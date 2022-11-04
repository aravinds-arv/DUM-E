# DUM-E
Just a rather very dumb [hydraulic arm](https://marvelcinematicuniverse.fandom.com/wiki/Dum-E_and_U). DUM-E can help you if you are a dev on discord!

### What can DUM-E do?

![dume](https://user-images.githubusercontent.com/78845005/199965503-55d14a44-536a-4c0d-a0ff-e7698abe0836.gif)

If you're a developer and use discord as your primary medium of communication, you must've realized how tiring and lethargic it feels to switch to your browser window and search for the bug 🐛 that you just hit while sharing your screen to your clients/project manager. Fear not for DUM-E has arrived to give you a helping hand (or more precisely a hydraulic arm 🦾). DUM-E reduces manual effort and increases developer productivity (factor: 20x) in the following ways:-

- It says `pong` when you say `!ping` signalling that it's up and running

![Screenshot 2022-11-04 181905](https://user-images.githubusercontent.com/78845005/199977325-602cec7e-fdb3-4897-99d6-a652172af70b.png)
- It motivates you when you feel low about your unresolved bugs. Just ask him to `!inspire`

![Screenshot 2022-11-04 182556](https://user-images.githubusercontent.com/78845005/199977674-7b717b81-6372-4f0d-ba6f-4e37616caa58.png)
- It delivers all the latest tech news from dev.to at specified intervals of time.

![Screenshot 2022-11-04 181954](https://user-images.githubusercontent.com/78845005/199977706-33c94b23-bda6-419b-8150-0fc05533765a.png)
- It picks yours query, places it on stackoverflow and returns all relevant answers directly to your server. The spell: `!sso "<YOUR QUERY>"`

![Screenshot 2022-11-04 181954](https://user-images.githubusercontent.com/78845005/199977777-9ffbe599-b491-489d-a422-8b542387aa88.png)

### How to configure?
- Copy .env.sample to a new file .env and replace the placeholder with your bot token
- Replace the `STACK_API_KEY` placeholder with your stack app key. Create a stack app by logging into the [Stackexchange API portal](http://stackapps.com/apps/oauth/register)
- (Optional) Create and use virtual environment for the project. Steps may vary depending on your OS, check out [this link](https://docs.python.org/3/tutorial/venv.html)
- Install all the requirements
- Replace the `tech_news_channel_id` with your appropriate channel id, find it by enabling developer mode in discord settings and right clicking on the channel you want to receive the tech news in.
```bash
$ pip install -r requirements.txt
```
- Run DUM-E 🎉
```bash
$ python main.py
```

### Boilerplate code for beginners
New to discord.py? Here's a boiler snippet you can use and extend as you please..
```python
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

load_dotenv()
TOKEN = os.getenv("TOKEN") # do configure your TOKEN in a .env file
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is logged in")

@client.command()
async def ping(ctx):
    await ctx.reply("pong")

client.run(TOKEN)
```

### A checklist of things to be done in the [developer portal](https://discord.com/developers)
- Create a new application
- Add a bot in the Bot tab
- Click on reset token and copy the token (use responsibly, if exposed your bot could be misused)
- Click on `OAuth`>`URL Generator` and check the option `bot` under `scopes`
- Give your required permissions


- Copy the generated URL and paste in a new browser tab
- Invite your bot to any of your servers

![Screenshot 2022-11-04 18411511](https://user-images.githubusercontent.com/78845005/199980640-ef2b2339-11c9-4000-953e-1109a42a4f63.png)

### Resources to get started with discord.py
- [Discord API Docs](https://discord.com/developers/docs/intro)
- [discord.py Docs](https://discordpy.readthedocs.io/en/stable/)
- [discord.py Official discord server](https://discord.gg/r3sSKJJ)
- [Freecodecamp Tutorial](https://www.youtube.com/watch?v=SPTfmiYiuok)

## Questions?
_**Ping me on discord:**_ _[Aravind S#3952](https://discord.com/users/900961892774854677)_
