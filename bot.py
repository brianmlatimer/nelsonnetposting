import discord
import os
from meme_functionality import meme

client = discord.Client(intents=discord.Intents.default())
botkey = os.getenv("botkey")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await meme.roulette(message, message.content)
    if message.content == "!bruh":
        await meme.shitpost(message,"this is a test")
    if message.content == "!last":
        await meme.send_last_meme(message)
client.run(botkey)
