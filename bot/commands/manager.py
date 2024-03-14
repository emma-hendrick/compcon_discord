from bot.commands.command_help import cmd_help
from bot.commands.get_character import get_character_data 

# Handle unknown commands
async def unknown_command(bot, channel, args, command):
    await channel.send(f"Unknown command \'{command}\'. Type !help for a list of commands.")

# Define a dictionary to map command names to their corresponding functions
commands = {
    "compcon": {
        "help": cmd_help,
        "getchar": get_character_data
        }
}

# Route the commands to the right function
async def process_command(bot, message):

    # Begin routing (if it begins with the command prefix)!
    if message.content.startswith("!"):

        # Split the message into command and arguements
        parts = message.content.split()
        command = parts[0][1:].lower() # Remove the prefix and convert to lowercase
        args = parts[1:]

        # Use a try-except block to handle unknown commands
        try:
            # If the command is valid command execute it, if it isnt a key throw an error, if it is another dict traverse one step further :)
            current_command_dict = commands
            while isinstance(current_command_dict[command], dict):
                if len(args) <= 0: # If there are no arguments to parse throw an error
                    raise KeyError(None)
                
                # Traverse a level deeper
                current_command_dict = current_command_dict[command]
                command = args.pop(0).lower() # Parse the first argument as the next level of the command

            # Get the corresponding function from the commands dictionary
            command_function = current_command_dict[command]
            # Execute the command function
            async with message.channel.typing():
                await command_function(bot, message.channel, args)
        except KeyError:
            await unknown_command(bot, message.channel, args, command)
