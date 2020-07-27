""" reddit.py

Bot commands relating to reddit
"""

from discord.ext import commands
from reddit_client import fetch


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def r(self, ctx):
        """Enables reddit subcommands, such as !r pic and !r search"""
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid reddit subcommand passed')

    @r.command()
    async def pic(self, ctx, subreddit_name: str):
        """Posts a link to a random image from the provided subreddit"""
        try:
            submission_url = fetch.get_random_media_submission(self.bot, subreddit_name)
            if submission_url is None:
                await ctx.send("No results found. Please select media-heavy subreddits only for this command.")
            else:
                await ctx.send(submission_url)
        except:
            await ctx.send("No results found. Subreddit is likely private/quarantined/non-existent/etc.")

    @r.command()
    async def search(self, ctx, subreddit_name: str, search_str: str):
        """Posts a link to a random submission from the provided subreddit"""
        try:
            submission_url = fetch.get_random_submission_by_title(self.bot, subreddit_name, search_str)
            if submission_url is None:
                await ctx.send("Something went wrong :(")
            else:
                await ctx.send('https://www.reddit.com' + submission_url)
        except:
            await ctx.send("An error has occurred. Search parameters might be bad. Subreddit also might be"
                               " private/quarantined/non-existent/etc.")


def setup(bot):
    bot.add_cog(Reddit(bot))
