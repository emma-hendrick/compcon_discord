# Print a message when the bot is initialized
async def on_ready(bot):
      print('We have logged in as {0.user.name}'.format(bot))

