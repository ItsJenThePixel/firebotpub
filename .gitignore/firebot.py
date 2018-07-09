import asyncio
import discord
import time
import random
from discord.exe import commands

client = discord.Client()
bot = commands.Bot(command_prefix="'")

@bot.event
async def on_ready():
  print('The bot is online and operational')
  print('The bot is currently named')
  print(bot.user.name)
  print('All errors will show under here')
  print('------------------------------')
  
