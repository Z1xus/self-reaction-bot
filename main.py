import discord
import random
import asyncio
from asyncio import Queue

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

# change yo user token
user_token = "..."

if use_proxy:
    client = discord.Client(proxy=proxy)
    print("using proxy: " + proxy)
else:
    client = discord.Client()

message_queue = Queue()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

async def add_reactions(message):
    global current_message
    current_message = message

    for reaction in reactions:
        await message.add_reaction(reaction)
        delay = random.randint(min_delay, max_delay)
        await asyncio.sleep(delay)

    while not message_queue.empty():
        next_message = await message_queue.get()
        await add_reactions(next_message)

@client.event
async def on_message(message):
    if message.channel.id in allowed_ids:
        await message_queue.put(message)
        if message_queue.qsize() == 1:
            await add_reactions(message)

try:
    client.run(user_token)
except Exception as e:
    print(f"An error occurred while running the bot: {e}")
