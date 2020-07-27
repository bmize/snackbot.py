""" misc.py

Miscellaneous and frivolous commands
"""

from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def idiot(self, ctx):
        """Agrees with the assertion that somebody is an idiot."""
        await ctx.send('yeah, IDIOT!')

    @commands.command()
    async def uwot(self, ctx):
        """Posts a .gif link in reaction to an absurd or terrible statement."""
        await ctx.send('https://i.imgur.com/IoAhjlR.gif')

    @commands.command(name='commands')
    async def command_list(self, ctx):
        """Displays a list of commands and their input formats"""
        commands =  "Command List\n" \
                    "  !r pic [subreddit]\n" \
                    "  !r search [subreddit] [title keywords]\n" \
                    "  !snack\n" \
                    "  !lenny\n" \
                    "  !roll [dice roll] - e.g. !roll 2d6\n" \
                    "  !idiot\n" \
                    "  !uwot\n"
        await ctx.send("```\n" + commands + "\n```")


def setup(bot):
    bot.add_cog(Misc(bot))
