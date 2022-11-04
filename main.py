import os
import discord
import requests
from dotenv import load_dotenv
from discord.ext import commands, tasks
from stackoverflow import fetch_res

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

load_dotenv()
TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix="!", intents=intents)

tech_news_channel_id = 1007960327520014446

@tasks.loop(minutes=2.0, reconnect=True)
async def post_tech_news():
    tech_news_channel = client.get_channel(tech_news_channel_id)
    r = requests.get("https://dev.to/api/articles?page=1&per_page=3&top=7%22")

    for post in r.json():
        title = post['title']
        excerpt = post['description']
        author = post['user']['username']
        tags = post['tags']
        url = post['url']
        cover = post['cover_image']
        reactions = post['public_reactions_count']
        embed_color = 0x5865F2
        embed = discord.Embed(title=title, url=url, color=discord.Color(embed_color))
        embed.set_image(url=cover)
        embed.add_field(name="__Excerpt__", value=f"```{excerpt}```", inline=False)
        embed.add_field(name="__Author__", value=author, inline=False)
        embed.add_field(name="__Tags__", value=tags, inline=False)
        embed.set_footer(text=f"❤️ {reactions} Reactions")
        await tech_news_channel.send(embed=embed)

@client.event
async def on_ready():
    print(f"{client.user} is logged in")
    post_tech_news.start()

@client.command()
async def ping(ctx):
    await ctx.reply("pong")

@client.command()
async def inspire(ctx):
    json_res = requests.get("https://zenquotes.io/api/quotes").json()
    quote = json_res[0]['q']
    author = json_res[0]['a']
    await ctx.channel.send(f"{quote} - _**{author}**_")

@client.command()
async def sso(ctx, query:str):
    res = fetch_res(query)
    embed_text = ""
    number = 0
    for response in res:
        title = response['title']
        url = response['url']
        number += 1
        embed_text += f"***Title:*** *{title}*\n ***URL:*** *{url}*\n\n"
    embed = discord.Embed(title="Here are the the top 5 matching results", description=embed_text, color=discord.Color.blurple())
    embed.set_footer(text=f"🔍 Search query: {query}")
    await ctx.channel.send(embed=embed)

client.run(TOKEN)