""" snackbot.py

Contains main function for running snackbot
"""

import praw
from discord_client import bot
import os


def reddit_login():
    return praw.Reddit(client_id=os.environ['REDDIT_CLIENT_ID'], client_secret=os.environ['REDDIT_CLIENT_SECRET'],
                       username=os.environ['REDDIT_USERNAME'], password=os.environ['REDDIT_PASSWORD'],
                       user_agent=os.environ['REDDIT_USER_AGENT'])


def run_bot():
    r = reddit_login()
    snackbot = bot.SnackBot(r)
    snackbot.run(os.environ['DISCORD_TOKEN'], reconnect=True)


if __name__ == '__main__':
    run_bot()
