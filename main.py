import asyncio

# Run the bot! And the server!
from bot.bot import run_bot
from bot.server import run_flask

# Run the server and the bot in a non-blocking way using asyncio
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(run_bot())
    loop.run_until_complete(loop.run_in_executor(None, run_flask))

