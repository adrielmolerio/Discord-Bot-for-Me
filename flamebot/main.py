import discord
import os
import re
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix = "$")

async def pick_insult(message):
    insultsAndKeys = {
    ("tired", "fat"): "Then get off Discord and go exercise.",
    ("Discord", "discord") : "Get off Discord and go do something productive already.",
    ("Admin", "admin", "administrator", "Mod", "mod", "moderator"): "We get it, you do it for free. Actually do something cool."
    }
    for key in insultsAndKeys:
        for i in key:
            if i in message.content:
                await message.channel.send(insultsAndKeys[key])

load_dotenv()

@bot.event
async def on_ready():
    print(f"We're logged in as {bot.user}.")
    print("End of on-ready.")

@bot.command()
@commands.guild_only()
async def ping(ctx):
    await ctx.channel.send("Pong!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: return
    await pick_insult(message)
    await bot.process_commands(message)

TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
