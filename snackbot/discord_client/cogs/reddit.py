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
        """Enables reddit subcommands, such as !r pic and !r search"""
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid reddit subcommand passed')

    @r.command()
    async def pic(self, subreddit_name: str):
        """Posts a link to a random image from the provided subreddit"""
        try:
            submission_url = fetch.get_random_media_submission(self.bot, subreddit_name)
            if submission_url is None:
                await self.bot.say("No results found. Please select media-heavy subreddits only for this command.")
            else:
                await self.bot.say(submission_url)
        except:
            await self.bot.say("No results found. Subreddit is likely private/quarantined/non-existent/etc.")

    @r.command()
    async def search(self, subreddit_name: str, search_str: str):
        """Posts a link to a random submission from the provided subreddit"""
        try:
            submission_url = fetch.get_random_submission_by_title(self.bot, subreddit_name, search_str)
            if submission_url is None:
                await self.bot.say("Something went wrong :(")
            else:
                await self.bot.say('https://www.reddit.com' + submission_url)
        except:
            await self.bot.say("An error has occurred. Search parameters might be bad. Subreddit also might be"
                               " private/quarantined/non-existent/etc.")


def setup(bot):
    bot.add_cog(Reddit(bot))
