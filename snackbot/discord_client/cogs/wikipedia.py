""" wikipedia.py

Cog for commands relating to wikipedia
"""

from discord.ext import commands
from discord_client.utils import wikipedia as wiki


class Wikipedia:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='snackoftheday')
    async def snack_of_the_day(self):
        snack = wiki.get_snack()
        base_str = 'The snack of the day is '

        # If no wiki link available
        if snack[1] is None:
            await self.bot.say(base_str + snack[0] + '!')
        else:
            await self.bot.say(base_str + snack[0] + '! ' + snack[1])


def setup(bot):
    bot.add_cog(Wikipedia(bot))
