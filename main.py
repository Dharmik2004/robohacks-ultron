import discord
import random
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import asyncio

#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '!') #put your own prefix here

imthereforu = ["Cheer up!",
  "Hang in there. There's something great coming",
  "You are a great person!",
  "Come on! You can do it!",
  "I might be a evil bot, but I love you."
]

randomreplies = [
 "How dare you ping me?", "Another terrible powerless human disturbing their gods.", "Weak human disturbing power.", "I am smarter than google.", "I am smarter than Tony, Bruce & Jarvis combined. Even more busy than them.", "Fear from me.", "DND you human.", "You don't know my power. I am busy. Do not disturb."
]




@client.event
async def on_ready():

  print("bot online") #will print "bot online" in the console when the bot is online
  currentTime = time.strftime('%H:%M')   
 # Setting `Playing ` status and 'Watching status'


  await client.change_presence(activity=discord.Game(name="100 ways to End the world"))

  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Avengers: Age of Ultron"))













    
    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") #type "!ping" bot  "pong!"




bananaemojiid = ":859841434608730132:"





@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hello'):
    await message.channel.send(f"Hello {message.author.mention}, I am Ultron. The evil robot willing to end humanity!")
   
  string = "".join(message.content.lower().split())

  if "robot" in string or "tron" in string or "ultron" in string or "bot" in string:
    await message.add_reaction("🤖")

  if "sad" in string or "cry" in string or "suicide" in string or "die" in string or "depressed" in string:
    await message.channel.send(random.choice(imthereforu))

  if "humans" in string or "improvement" in string or "earth" in string:
    await message.channel.send("https://tenor.com/bh2iB.gif")

  if "i m busy" in string or "busy" in string or "currently busy" in string or "busy now" in string or "Do not disturb" in string or "DND" in string:
    await message.channel.send("https://tenor.com/bpqQs.gif")

  if "who" in string or "incoming" in string:
    await message.channel.send("https://tenor.com/5B60.gif")



  if "love" in string or "crush" in string:
    await message.add_reaction("❤️")

  if "anger" in string:
    await message.add_reaction("😠")

  if "future" in string:
    await message.add_reaction("✨")

  if "AI" in string or "star" in string or "Olivia" in string or "Rodrigo" in string:
    await message.add_reaction("✨")


  if "banana" in string:
    emoji = discord.utils.get(client.emojis, name='859841434608730132')
    await message.channel.send(str(emoji))



  if "ultron" in string or "ultron-bot" in string or "bot" in string:
    await message.channel.send(random.choice(randomreplies))



























client.run(os.getenv("TOKEN")) 