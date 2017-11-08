""" fetch.py

Used to fetch posts/images/etc. from reddit.com
"""

from urllib.parse import urlparse
import time

accepted_sources = (
    'i.redd.it',
    'i.imgur.com',
    'media.giphy.com',
)


def get_random_media_submssion(bot, subreddit_name: str):
    subreddit = bot.reddit.subreddit(subreddit_name)
    submission = subreddit.random()

    uri = urlparse(submission.url)
    netloc = uri.netloc

    start = time.time()
    while netloc not in accepted_sources:
        if time.time() - start >= 5:
            return None
        submission = subreddit.random()
        netloc = urlparse(submission.url).netloc

    return submission.url
