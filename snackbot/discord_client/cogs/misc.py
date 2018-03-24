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
    async def uwot(self):
        await self.bot.say('https://i.imgur.com/IoAhjlR.gif')

    @commands.command(name='commands')
    async def command_list(self):
        commands =  "**Command List**\n" \
                    "  !r pic [subreddit]\n" \
                    "  !r search [subreddit] [title keywords]\n" \
                    "  !snack\n" \
                    "  !lenny\n" \
                    "  !roll [dice roll] - e.g. !roll 2d6\n" \
                    "  !idiot\n" \
                    "  !uwot\n"
        await self.bot.say(commands)


def setup(bot):
    bot.add_cog(Misc(bot))
