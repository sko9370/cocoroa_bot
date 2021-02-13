import discord
import os
import time

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    # do nothing if message is created by this bot
    if message.author == client.user:
        return

    # regex for start with hello
    elif message.content.startswith("$hello"):
        await message.channel.send("Hello!")
    
    elif message.content == "$home":
        time.sleep(5)
        await message.channel.send("do an exercise")

client.run(os.getenv("TOKEN"))