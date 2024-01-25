import discord
import random
import asyncio
import logging
import os
from dotenv import load_dotenv
from asyncio import Semaphore, Queue

if os.path.exists(".env"):
    load_dotenv()
else:
    logging.error("No .env file found.")

# since v1.0.3 configuration was moved to .env

use_proxy = os.getenv("USE_PROXY") == "True"
proxy = os.getenv("PROXY")
allowed_ids = list(map(int, os.getenv("ALLOWED_IDS").split(",")))
reactions = os.getenv("REACTIONS").split(",")
min_delay = int(os.getenv("MIN_DELAY"))
max_delay = int(os.getenv("MAX_DELAY"))
user_token = os.getenv("USER_TOKEN")

semaphore = Semaphore(5)

if use_proxy:
    client = discord.Client(chunk_guild_at_startup=False, proxy=proxy)
    print(f"Using proxy: {proxy}")
else:
    client = discord.Client(chunk_guild_at_startup=False)

message_queue = Queue()


async def add_reactions(message):
    async with semaphore:
        message_deleted = False
        for reaction in reactions:
            if message_deleted:
                break
            try:
                await message.add_reaction(reaction)
                delay = random.randint(min_delay, max_delay)
                await asyncio.sleep(delay)
            except discord.errors.NotFound:
                logging.error("Message not found. Skipping reactions.")
                message_deleted = True
            except discord.errors.Forbidden:
                logging.error("Permisssions error. Skipping reactions.")
                message_deleted = True
            except discord.errors.HTTPException:
                logging.warning("Rate limit or network error. Retrying after delay.")
                await asyncio.sleep(10)
                await message.add_reaction(reaction)
            except Exception as e:
                logging.exception(
                    f"An unexpected error occurred while adding reaction: {e}"
                )


async def process_messages():
    while True:
        message = await message_queue.get()
        await add_reactions(message)
        message_queue.task_done()


@client.event
async def on_message(message):
    if message.channel.id in allowed_ids:
        await message_queue.put(message)


@client.event
async def on_ready():
    try:
        print(f"Logged in as {client.user}")
        asyncio.create_task(process_messages())
    except discord.LoginFailure:
        logging.warning("Login failed. Make sure you're using a valid user token.")
    except Exception as e:
        logging.exception(f"An error occurred while running the bot: {e}")


try:
    if not user_token:
        raise ValueError("No user token provided")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.start(user_token))
except ValueError as ve:
    logging.error(ve)
except discord.LoginFailure:
    logging.error("Login failed. Make sure you're using a valid user token.")
except KeyboardInterrupt:
    print("\nCtrl+C received, exiting...")
except Exception as e:
    logging.exception(f"An error occurred while running the bot: {e}")
