""" fetch.py

Used to fetch posts/images/etc. from reddit.com
"""

from urllib.parse import urlparse
import time
import random
from logging import Logger

accepted_sources = (
    'i.redd.it',
    'imgur.com',
    'i.imgur.com',
    'media.giphy.com',
    'gfycat.com',
    'giant.gfycat.com'
)

blacklisted_titles = (
    'nigri',
)


def get_random_media_submssion(bot, subreddit_name: str):
    subreddit = bot.reddit.subreddit(subreddit_name)
    submission = subreddit.random()

    uri = urlparse(submission.url)
    netloc = uri.netloc

    start = time.time()
    while netloc not in accepted_sources or any(x in submission.title.lower() for x in blacklisted_titles):
        if time.time() - start >= 3:
            return None
        submission = subreddit.random()
        netloc = urlparse(submission.url).netloc

    return submission.url

def get_random_submission_by_title(bot, subreddit_name: str, search_str:str):
    results = []
    for result in bot.reddit.subreddit(subreddit_name).search('title:' + search_str):
        results.append(result.permalink)

    Logger.debug('subreddit: ' + subreddit_name + ' search string: ' + search_str + ' results length: '
                 + str(len(results)))

    return random.choice(results)
