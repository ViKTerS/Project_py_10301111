import discord
import os
from discord.ext import commands


from myserver import server_on


bot = commands.bot(command_prefix = '/',intents = discord.intents.all())

@bot.event
async def on_ready():
    print("Bot online")
    
server_on()

bot.run(os.getenv('TOKEN'))
    