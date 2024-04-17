from bot.compcon.get_character import get_character_by_code
from bot.compcon.character_png import generate_png
from bot.compcon.character_html import generate_html
import discord
from io import BytesIO
import time

#Get the character data and return it
async def get_character_data(bot, channel, args):
    
    # Get start time
    start_time = time.time()

    # Get the character json
    character_json = get_character_by_code(args[0])
    json_time = time.time()

    # Convert the json into a character sheet using html
    html = generate_html(character_json)
    html_time = time.time()

    # Convert the html into a png
    png = BytesIO(generate_png(html))
    filename = character_json["name"].lower().strip().replace(" ", "_")
    png_time = time.time()

    # Send the file
    await channel.send(file=discord.File(png, filename=f"{filename}.png"))

    # Get elapsed time for each step
    elapsed_json = json_time - start_time
    elapsed_html = html_time - json_time
    elapsed_png = png_time - html_time

    # Print time for all tasks
    print(f"JSON: {elapsed_json}")
    print(f"HTML: {elapsed_html}")
    print(f"PNG: {elapsed_png}")
