from bot.utils.constants import CONST
from bot.commands.manager import process_command
import discord


# When a message is sent, check its contents, and correct it if it references M
async def on_message(bot, message):

    # Check if the message is from the bot itself
    if message.author == bot.user:
        return

    # Process the command!
    await process_command(bot, message)
