## self-reaction-bot

A Discord Python Selfbot to put reactions on messages.  
Designed specifically to annoy all your friends.

> [!WARNING]  
> This may not work with the latest discord.py-self.  
> In that case you should install a development version by cloning the discord.py-self repository and running `python -m pip install -U .`

<picture>
  <source srcset="https://raw.githubusercontent.com/Z1xus/self-reaction-bot/main/preview.webp">
  <img alt="preview">
</picture>

<p align="center">
    <a href="https://github.com/psf/black" alt="Code style: black">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" /></a>
    <a href="https://www.codefactor.io/repository/github/z1xus/self-reaction-bot/">
        <img src="https://www.codefactor.io/repository/github/z1xus/self-reaction-bot/badge" alt="CodeFactor" /></a>
    <a href="https://github.com/Z1xus/self-reaction-bot/issues?q=is%3Aissue+is%3Aopen+" alt="GitHub issues">
        <img src="https://img.shields.io/github/issues/z1xus/self-reaction-bot"></a>
    <a href="https://github.com/Z1xus/self-reaction-bot/pulls?q=is%3Apr+is%3Aopen+" alt="GitHub pull requests">
        <img src="https://img.shields.io/github/issues-pr/z1xus/self-reaction-bot"></a>
</p>

### Features:
+ Proxy support
+ Message queue to avoid rate limits
+ Random delay between reactions

### Use it on your own risk.
You have to understand that selfbots are against Discord TOS, and there is a great chance your account will get terminated using one.

### Usage:
1. Clone the repository
```bash
git clone https://github.com/Z1xus/self-reaction-bot
```
2. Install dependencies
```bash
pip install -r .\requirements.txt -U
```
3. Configure your .env
```Shell
# in case you got rate limited
USE_PROXY=False
PROXY=http://localhost:8080

# channel ids where the bot listens for messages
ALLOWED_IDS=1234567890123456789,...

# reactions list in unicode, emoji and escape formats
REACTIONS=🇧,🇮,🇹,🇨,🇭

# random delay range in seconds
MIN_DELAY=1
MAX_DELAY=5

# your discord user token, see https://www.androidauthority.com/get-discord-token-3149920/
USER_TOKEN=
```
4. Run it 
```bash
python3 .\main.py
```
