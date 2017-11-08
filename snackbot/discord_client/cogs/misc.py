""" misc.py

Miscellaneous and frivolous commands
"""

from discord.ext import commands


class Misc:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def idiot(self):
        await self.bot.say('yeah, IDIOT!')

    @commands.command()
    async def havemercypls(self):
        await self.bot.say('http://readeroffictions.com/wp-content/uploads/2016/02/gif-ill-kill-you-office.gif')


def setup(bot):
    bot.add_cog(Misc(bot))
