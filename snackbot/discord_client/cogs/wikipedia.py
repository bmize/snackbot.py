""" wikipedia.py

Cog for commands relating to wikipedia
"""

from discord.ext import commands
from discord_client.utils import wikipedia as wiki


class Wikipedia:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='snack')
    async def snack(self):
        snack = wiki.get_snack()
        base_str = 'Your snack is '

        if snack[1] is None:    # If no wiki link available
            await self.bot.say(base_str + snack[0] + '!')
        else:
            await self.bot.say(base_str + snack[0] + '! ' + snack[1])


def setup(bot):
    bot.add_cog(Wikipedia(bot))
