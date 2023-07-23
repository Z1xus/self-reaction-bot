## A Discord Python Selfbot to put reactions on messages

Designed specifically to annoy all your friends with constant reactions on messages.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://media.discordapp.net/attachments/1118618417650483285/1131691836306632777/2.png?width=719&height=310">
  <source media="(prefers-color-scheme: light)" srcset="https://media.discordapp.net/attachments/1118618417650483285/1131691836306632777/2.png?width=719&height=310">
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
pip install -r .\requirements.txt
```
3. Configure the bot
```python
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
```
4. Run it 
```bash
python3 .\main.py
```
