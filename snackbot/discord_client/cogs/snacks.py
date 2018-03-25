""" snacks.py

Cog for commands relating to snacks
"""

from discord.ext import commands
from discord_client.utils import snacks


class Snacks:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='snack')
    async def snack(self):
        """Displays a random snack and an associated link for that snack"""
        snack = snacks.get_snack()
        base_str = 'Your snack is '

        if snack is None:
            await self.bot.say("A database error has occurred. PLEASE TELL BSNACKIN. THIS IS A PROBLEM.")
        else:
            if snack[1] is None:    # If no link is available
                await self.bot.say(base_str + snack[0] + '!')
            else:
                await self.bot.say(base_str + snack[0] + '! ' + snack[1])


def setup(bot):
    bot.add_cog(Snacks(bot))
