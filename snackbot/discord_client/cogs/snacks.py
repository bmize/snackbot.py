""" snacks.py

Cog for commands relating to snacks
"""

from discord.ext import commands
from discord_client.utils import snacks


class Snacks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='snack')
    async def snack(self, ctx):
        """Displays a random snack and an associated link for that snack"""
        snack = snacks.get_snack()
        base_str = 'Your snack is '

        if snack is None:
            await ctx.send("A database error has occurred. PLEASE TELL BSNACKIN. THIS IS A PROBLEM.")
        else:
            if snack[1] is None:    # If no link is available
                await ctx.send(base_str + snack[0] + '!')
            else:
                await ctx.send(base_str + snack[0] + '! ' + snack[1])


def setup(bot):
    bot.add_cog(Snacks(bot))
