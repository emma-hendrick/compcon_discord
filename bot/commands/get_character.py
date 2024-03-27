from bot.compcon.get_character import get_character_by_code
from bot.compcon.character_png import generate_png
from bot.compcon.character_html import generate_html
import discord
from io import BytesIO

#Get the character data and return it
async def get_character_data(bot, channel, args):

    # Get the character json
    character_json = get_character_by_code(args[0])
    print("json:", character_json)

    # Convert the json into a character sheet using html
    html = generate_html(character_json)

    # Convert the html into a png
    png = BytesIO(generate_png(html))
    filename = character_json["name"].lower().strip().replace(" ", "_")

    # Send the file
    await channel.send(file=discord.File(png, filename=f"{filename}.png"))
