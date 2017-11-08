import praw

import discord
from discord_client import discord_auth
from reddit_client import reddit_auth
from discord_client import bot


def reddit_login():
    return praw.Reddit(client_id=reddit_auth.CLIENT_ID, client_secret=reddit_auth.CLIENT_SECRET,
                       username=reddit_auth.USERNAME, password=reddit_auth.PASSWORD, user_agent=reddit_auth.USER_AGENT)


def discord_login():
    client = discord.Client()
    client.run(discord_auth.TOKEN)


if __name__ == '__main__':
    r = reddit_login()
    snackbot = bot.SnackBot(r)
    bot.start_bot(snackbot, discord_auth.TOKEN)
