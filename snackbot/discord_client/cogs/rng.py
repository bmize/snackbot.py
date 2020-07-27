""" rng.py

Bot commands involving random chance
"""

from collections import namedtuple
import random
from discord.ext import commands
from discord_client.utils import dnd


class RNG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """
    @commands.group(pass_context=True)
    async def rng(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid random subcommand passed.')
    """

    @commands.command()
    async def lenny(self, ctx):
        """Displays a random lenny face."""
        lenny = random.choice([
            "( ͡° ͜ʖ ͡°)", "( ͠° ͟ʖ ͡°)", "ᕦ( ͡° ͜ʖ ͡°)ᕤ", "( ͡~ ͜ʖ ͡°)",
            "( ͡o ͜ʖ ͡o)", "͡(° ͜ʖ ͡ -)", "( ͡͡ ° ͜ ʖ ͡ °)﻿", "(ง ͠° ͟ل͜ ͡°)ง",
            "ヽ༼ຈل͜ຈ༽ﾉ"
        ])
        await ctx.send(lenny)

    @commands.command()
    async def roll(self, ctx, die_info):
        """Displays the result of rolling dice in standard D&D style (e.g. '2d6')"""
        Die = namedtuple('Dice', 'num sides')
        try:
            die = Die(*dnd.parse_roll_syntax(die_info))
            rolls = dnd.roll_dice(die.num, die.sides)
            await ctx.send("```\n" + ', '.join(rolls) + "\n```")
        except TypeError:
            await ctx.send('Incorrect die format. Sample format: !roll 2d6')


def setup(bot):
    bot.add_cog(RNG(bot))
