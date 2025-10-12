from __future__ import annotations

import asyncio
import logging
import os
import random
from asyncio import Queue, Semaphore
from typing import TYPE_CHECKING

import colorlog
import discord
from dotenv import load_dotenv

if TYPE_CHECKING:
    from collections.abc import Sequence

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(log_color)s[%(levelname)s]%(reset)s %(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
    )
)

logging.basicConfig(level=logging.INFO, handlers=[handler])

if not os.path.exists(".env"):
    logging.error("No .env file found. Copy .env.example to .env and configure it.")
    raise SystemExit(1)

load_dotenv()


def get_env_var(key: str, required: bool = True) -> str | None:
    value = os.getenv(key)
    if required and not value:
        logging.error(f"Missing required environment variable: {key}")
        raise SystemExit(1)
    return value


def parse_bool(value: str | None) -> bool:
    return value == "True"


def parse_int_list(value: str | None) -> list[int]:
    if not value:
        return []
    return [int(x.strip()) for x in value.split(",") if x.strip()]


def parse_string_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [x.strip() for x in value.split(",") if x.strip()]


use_proxy = parse_bool(get_env_var("USE_PROXY", required=False))
proxy = get_env_var("PROXY", required=False) if use_proxy else None
allowed_ids = parse_int_list(get_env_var("ALLOWED_IDS"))
reactions = parse_string_list(get_env_var("REACTIONS"))
min_delay = int(get_env_var("MIN_DELAY") or "1")
max_delay = int(get_env_var("MAX_DELAY") or "5")
user_token = get_env_var("USER_TOKEN")

if not allowed_ids:
    logging.error("No ALLOWED_IDS configured. Please add at least one channel ID.")
    raise SystemExit(1)

if not reactions:
    logging.error("No REACTIONS configured. Please add at least one reaction.")
    raise SystemExit(1)

if min_delay < 0 or max_delay < min_delay:
    logging.error(f"Invalid delay configuration: MIN_DELAY={min_delay}, MAX_DELAY={max_delay}")
    raise SystemExit(1)

semaphore = Semaphore(5)
message_queue: Queue[discord.Message] = Queue()

client = discord.Client(
    chunk_guilds_at_startup=False,
    proxy=proxy if use_proxy else None,
)

if use_proxy and proxy:
    logging.info(f"Using proxy: {proxy}")


async def add_reactions(message: discord.Message, reaction_list: Sequence[str]) -> None:
    async with semaphore:
        message_deleted = False
        for reaction in reaction_list:
            if message_deleted:
                break
            try:
                await message.add_reaction(reaction)
                delay = random.uniform(min_delay, max_delay)
                await asyncio.sleep(delay)
            except discord.NotFound:
                logging.warning("Message not found, skipping remaining reactions")
                message_deleted = True
            except discord.Forbidden:
                logging.warning("Missing permissions, skipping remaining reactions")
                message_deleted = True
            except discord.HTTPException as e:
                if e.status == 429:  # rate limited
                    logging.warning(f"Rate limited, waiting {e.retry_after or 10}s before retry")
                    await asyncio.sleep(e.retry_after or 10)
                    try:
                        await message.add_reaction(reaction)
                    except discord.HTTPException:
                        logging.error(f"Failed to add reaction after retry: {reaction}")
                else:
                    logging.error(f"HTTP error while adding reaction: {e}")
            except Exception:
                logging.exception("Unexpected error while adding reaction")


async def process_messages() -> None:
    while True:
        message = await message_queue.get()
        await add_reactions(message, reactions)
        message_queue.task_done()


@client.event
async def on_message(message: discord.Message) -> None:
    if message.channel.id in allowed_ids:
        await message_queue.put(message)


@client.event
async def on_ready() -> None:
    logging.info(f"Logged in as {client.user}")
    asyncio.create_task(process_messages())


async def main() -> None:
    try:
        logging.info("Attempting to login with provided token...")
        await client.start(user_token)
    except discord.LoginFailure:
        logging.error("Login failed. Make sure you're using a valid user token.")
        raise SystemExit(1)
    except Exception:
        logging.exception("An error occurred while running the bot")
        raise
    finally:
        await client.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Received interrupt signal, shutting down...")
    except SystemExit:
        raise
    except Exception:
        logging.exception("Unexpected error during execution")
        raise SystemExit(1)
