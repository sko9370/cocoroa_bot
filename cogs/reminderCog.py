#import discord
from discord.ext import tasks, commands

class reminderCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #self.channel = discord.utils.get(bot.get_all_channels(), name="general")
        self.channel = None
        self.first = True

    @commands.Cog.listener()
    async def on_ready(self):
        print("We have logged in as {0.user}".format(self.bot))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        elif message.content == 'Home':
            await message.channel.send("Welcome back")
            self.channel = message.channel
            self.first = True
            self.reminder.start()
        elif message.content == 'Sleep':
            await message.channel.send("Good night")
            self.reminder.cancel()
        elif message.content == 'Work':
            await message.channel.send("Safe drive")
            self.reminder.cancel()

    @tasks.loop(hours=1)
    async def reminder(self):
        if self.first:
            self.first = False
            return
        else:
            await self.channel.send("Do an exercise")

def setup(bot):
    bot.add_cog(reminderCog(bot))
