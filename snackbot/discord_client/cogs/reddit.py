""" reddit.py

Bot commands relating to reddit
"""

from discord.ext import commands

from reddit_client import fetch


class Reddit:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def r(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid reddit subcommand passed')

    @r.command()
    async def pic(self, subreddit_name: str):
        submission_url = fetch.get_random_media_submssion(self.bot, subreddit_name)
        await self.bot.say(submission_url)


def setup(bot):
    bot.add_cog(Reddit(bot))
