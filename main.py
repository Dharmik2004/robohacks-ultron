import discord
import random
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check


#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '!') #put your own prefix here

imthereforu = ["Cheer up!",
  "Hang in there. There's something great coming",
  "You are a great person!",
  "Come on! You can do it!",
  "I might be a evil bot, but I love you"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    
    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"




async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")



@client.event
async def on_message(message):

  async def mm(ctx):
    if message.content.startswith('motivateme'):
      quote = get_quote()
      await message.channel.ctx.send(quote)



@client.event
async def on_message(message):
   
  string = "".join(message.content.lower().split())


  if "robot" in string or "tron" in string or "ultron" in string:
    await message.add_reaction("🤖")

  if "sad" in string or "cry" in string or "suicide" in string or "die" in string or "depressed" in string:
    await message.channel.send(random.choice(imthereforu))






































client.run(os.getenv("TOKEN")) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!