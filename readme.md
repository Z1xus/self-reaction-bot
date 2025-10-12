## self-reaction-bot

A Discord Python Selfbot to put reactions on messages.  
Designed specifically to annoy all your friends.

<picture>
  <source srcset="https://raw.githubusercontent.com/Z1xus/self-reaction-bot/main/preview.webp">
  <img alt="preview">
</picture>

<p align="center">
    <a href="https://github.com/astral-sh/ruff" alt="Ruff">
        <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square" /></a>
    <a href="https://www.codefactor.io/repository/github/z1xus/self-reaction-bot/">
        <img src="https://www.codefactor.io/repository/github/z1xus/self-reaction-bot/badge?style=flat-square" alt="CodeFactor" /></a>
    <a href="https://github.com/Z1xus/self-reaction-bot/issues?q=is%3Aissue+is%3Aopen+" alt="GitHub issues">
        <img src="https://img.shields.io/github/issues/z1xus/self-reaction-bot?style=flat-square&color=yellow"></a>
    <a href="https://github.com/Z1xus/self-reaction-bot/pulls?q=is%3Apr+is%3Aopen+" alt="GitHub pull requests">
        <img src="https://img.shields.io/github/issues-pr/z1xus/self-reaction-bot?style=flat-square&color=blue"></a>
    <a href="https://github.com/Z1xus/self-reaction-bot/commits/main" alt="GitHub last commit">
        <img src="https://img.shields.io/github/last-commit/z1xus/self-reaction-bot?style=flat-square&color=green"></a>
</p>

### Features:
+ Proxy support
+ Message queue to avoid rate limits
+ Random delay between reactions

### Use it on your own risk.
You have to understand that selfbots are against Discord TOS, and there is a great chance your account will get terminated using one.

### Requirements:
- [uv](https://docs.astral.sh/uv/getting-started/installation/) - Fast Python package manager

### Usage:
1. Clone the repository
```bash
git clone https://github.com/Z1xus/self-reaction-bot
```
2. Install dependencies with uv
```bash
uv sync
```
3. Configure your .env
```Shell
# proxy configuration (in case you get rate limited)
USE_PROXY=False
PROXY=http://localhost:8080

# channel ids where the bot listens for messages (comma-separated)
ALLOWED_IDS=1234567890123456789

# reactions list in unicode, emoji and escape formats (comma-separated)
REACTIONS=🇧,🇮,🇹,🇨,🇭

# random delay range in seconds
MIN_DELAY=1
MAX_DELAY=5

# your discord user token, see https://www.androidauthority.com/get-discord-token-3149920/
USER_TOKEN=
```
4. Run it 
```bash
uv run main.py
```

> [!TIP]  
> You can find all Discord emojis and copy them from https://emojipedia.org/discord
