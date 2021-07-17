import discord
import os
import re
import random
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

@bot.command()
@commands.guild_only()
async def eightball(ctx):
    predictions = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely", "Outlook good.", 
    "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
    "My sources say no.", "Outlook not so good.", "Very doubtful."]
    await ctx.channel.send(predictions[random.randint(1, 20)]) 

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot: return
    await pick_insult(message)
    await bot.process_commands(message)

TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
