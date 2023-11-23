import discord
import os 
from dotenv import load_dotenv

intents = discord.Intents.default()     # Specifies the intents to be used by the bot
intents.message_content = True          # Allows bot to read message contents

load_dotenv() # load .env file
bot = discord.Bot(intents=intents)

cogs_list = [       # List of cogs
    'commands',
    'events'
]

for cog in cogs_list:   # Loads the cogs
    bot.load_extension(f'cogs.{cog}')


bot.run(os.getenv('BOT_TOKEN'))