import discord
import random
import asyncio
from asyncio import Semaphore, Queue

# in case you got rate limited
use_proxy = False
proxy = "http://localhost:8080"

# channel ids where the bot listens for messages
allowed_ids = [1234567890123456789, ...]

# reactions list in unicode, emoji and escape formats
reactions = ["🇧", "🇮", "🇹", "🇨", "🇭"]

# random delay range in seconds
min_delay = 1
max_delay = 5

# change your user token
user_token = "..."

semaphore = Semaphore(5)

if use_proxy:
    client = discord.Client(proxy=proxy)
    print(f"Using proxy: {proxy}")
else:
    client = discord.Client()

message_queue = Queue()

async def add_reactions(message):
    async with semaphore:
        for reaction in reactions:
            try:
                await message.add_reaction(reaction)
                delay = random.randint(min_delay, max_delay)
                await asyncio.sleep(delay)
            except discord.errors.NotFound:
                print("Message not found. Skipping reaction.")
            except Exception as e:
                print(f"An error occurred while adding reaction: {e}")

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
    print(f"Logged in as {client.user}")
    asyncio.create_task(process_messages())

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.start(user_token))
except KeyboardInterrupt:
    print("\nCtrl+C received, exiting...")
except Exception as e:
    print(f"An error occurred while running the bot: {e}")
