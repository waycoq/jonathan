from discord.ext import commands

class Events(commands.Cog):
    
    def __init__(self, bot):    # Initializes Cog
        self.bot = bot

    @commands.Cog.listener()    # Verifies the status of the bot
    async def on_ready(self):
        print(f'{self.bot.user} is online')
    
    @commands.Cog.listener()    # Listens to messages
    async def on_message(self, ctx):
        
        if ctx.author == self.bot.user:
            return
        
        if ctx.content.startswith('hi'):    # Responds to message if it starts with 'hi'
            await ctx.channel.send('uwu')


def setup(bot):
    bot.add_cog(Events(bot))
