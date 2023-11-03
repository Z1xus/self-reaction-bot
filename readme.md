## A Discord Python Selfbot to put reactions on messages

Designed specifically to annoy all your friends with constant reactions on messages.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://media.discordapp.net/attachments/1118618417650483285/1131691836306632777/2.png?width=719&height=310">
  <source media="(prefers-color-scheme: light)" srcset="https://media.discordapp.net/attachments/1118618417650483285/1132781143314411640/4.png?width=719&height=310">
  <img alt="Demonstration">
</picture>

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
