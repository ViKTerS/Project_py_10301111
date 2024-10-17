import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on


bot = commands.bot(command_prefix = '/',intents = discord.intents.all())

TOKEN = MTI5NjQ1MzgwNjQ0NzUyNTkzOA.G0wRfk.aSn1O8H-XuuaOpCtajT5T91r0if7oQ4vxG3b14

@bot.event
async def on_ready():
    print("Bot online")
    
server_on()

bot.run(TOKEN)
    