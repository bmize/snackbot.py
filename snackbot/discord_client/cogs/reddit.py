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
        submission_url = fetch.get_random_media_submission(self.bot, subreddit_name)
        if submission_url is None:
            await self.bot.say("No results found. Please select media-heavy subreddits only for this command.")
        else:
            await self.bot.say(submission_url)

    @r.command()
    async def search(self, subreddit_name: str, search_str: str):
        submission_url = fetch.get_random_submission_by_title(self.bot, subreddit_name, search_str)
        if submission_url is None:
            await self.bot.say("something went wrong")
        else:
            await self.bot.say('https://www.reddit.com' + submission_url)


def setup(bot):
    bot.add_cog(Reddit(bot))
