# Discord allows us to actually control our discord bot
import discord
from bot.events.on_ready import on_ready as on_ready_event
from bot.events.on_message import on_message as on_message_event
from bot.utils.constants import CONST

# Set the intents and client for out bot
intents = discord.Intents.all()
bot = discord.Client(intents=intents)


# When the bot is activated and connected to its client
@bot.event
async def on_ready():
    await on_ready_event(bot)


# When the bot receives a message
@bot.event
async def on_message(message):
    await on_message_event(bot, message)


# A nice function for our bff threads
async def run_bot():

    # Run the bot with our token
    await bot.start(CONST.DISCORD_TOKEN)

