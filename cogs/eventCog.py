from discord.ext import tasks, commands
import time

class eventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.on = False

    @commands.Cog.listener()
    async def on_ready(self):
        print("We have logged in as {0.user}".format(self.bot))
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        elif message.content == 'home':
            self.on = True
            while self.on:
                time.sleep(5)
                await message.channel.send("do an exercise")          

        elif message.content == 'sleep':
            await message.channel.send("Good night")
            self.on = False
        
        elif message.content == 'work':
            await message.channel.send("safe drive")
            self.on = False

def setup(bot):
    bot.add_cog(eventCog(bot))