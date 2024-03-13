# OS allows us to retrieve our evironment variables
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load variables from .env
dotenv_path = join(dirname(__file__), "../../.env")
print(dotenv_path)
load_dotenv(dotenv_path)

# All the program constants
class CONST:
    DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
    API_KEY = os.environ['X_API_KEY']


