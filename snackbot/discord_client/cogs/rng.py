""" rng.py

Bot commands involving random chance
"""

from discord.ext import commands
import random


class RNG:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def rng(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid random subcommand passed.')

    @rng.command()
    async def lenny(self):
        """Displays a random lenny face."""
        lenny = random.choice([
            "( ͡° ͜ʖ ͡°)", "( ͠° ͟ʖ ͡°)", "ᕦ( ͡° ͜ʖ ͡°)ᕤ", "( ͡~ ͜ʖ ͡°)",
            "( ͡o ͜ʖ ͡o)", "͡(° ͜ʖ ͡ -)", "( ͡͡ ° ͜ ʖ ͡ °)﻿", "(ง ͠° ͟ل͜ ͡°)ง",
            "ヽ༼ຈل͜ຈ༽ﾉ"
        ])
        await self.bot.say(lenny)


def setup(bot):
    bot.add_cog(RNG(bot))
