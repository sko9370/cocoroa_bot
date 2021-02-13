import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix='!')

bot.load_extension('cogs.reminderCog')

bot.run(os.getenv('TOKEN'))
