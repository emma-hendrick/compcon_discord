from bot.compcon.get_character import get_character_by_code

#Get the character data and return it
async def get_character_data(bot, channel, args):
    result = get_character_by_code(args[0])
    print(result)
    await channel.send(result)
