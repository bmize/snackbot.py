""" snackbot_local.py

Used for locally testing snackbot before deploying to server
"""
import logging
import praw
from discord_client import bot, discord_auth
from reddit_client import reddit_auth


def reddit_login():
    return praw.Reddit(client_id=reddit_auth.CLIENT_ID, client_secret=reddit_auth.CLIENT_SECRET,
                       username=reddit_auth.USERNAME, password=reddit_auth.PASSWORD, user_agent=reddit_auth.USER_AGENT)


def run_bot():
    r = reddit_login()
    snackbot = bot.SnackBot(r, '.')
    snackbot.run(discord_auth.TOKEN, reconnect=True)


if __name__ == '__main__':
    logging.basicConfig(filename='snackbot.log', level=logging.DEBUG)
    logging.info('\n\n\n----Logging started----')
    run_bot()
    logging.info('----Logging finished----\n\n')
