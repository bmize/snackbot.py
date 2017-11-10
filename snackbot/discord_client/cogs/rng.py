""" rng.py

Bot commands involving random chance
"""

from collections import namedtuple
import random
from discord.ext import commands

from discord_client.utils import dnd


class RNG:
    def __init__(self, bot):
        self.bot = bot

    """
    @commands.group(pass_context=True)
    async def rng(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid random subcommand passed.')
    """

    @commands.command()
    async def lenny(self):
        """Displays a random lenny face."""
        lenny = random.choice([
            "( ͡° ͜ʖ ͡°)", "( ͠° ͟ʖ ͡°)", "ᕦ( ͡° ͜ʖ ͡°)ᕤ", "( ͡~ ͜ʖ ͡°)",
            "( ͡o ͜ʖ ͡o)", "͡(° ͜ʖ ͡ -)", "( ͡͡ ° ͜ ʖ ͡ °)﻿", "(ง ͠° ͟ل͜ ͡°)ง",
            "ヽ༼ຈل͜ຈ༽ﾉ"
        ])
        await self.bot.say(lenny)

    @commands.command()
    async def roll(self, die_info):
        """Displays the result of rolling count dice with count sides"""
        Die = namedtuple('Dice', 'num sides')
        try:
            die = Die(*dnd.parse_roll_syntax(die_info))
            rolls = dnd.roll_dice(die.num, die.sides)
            await self.bot.say(', '.join(rolls))
        except TypeError:
            await self.bot.say('Incorrect die format. Sample format: !roll 2d6')


def setup(bot):
    bot.add_cog(RNG(bot))
