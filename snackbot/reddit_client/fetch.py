""" fetch.py

Used to fetch posts/images/etc. from reddit.com
"""

import random
import logging

accepted_sources = (
    'i.redd.it',
    'imgur.com',
    'i.imgur.com',
    'giphy.com',
    'media.giphy.com',
    'gfycat.com',
    'giant.gfycat.com',
    'redgifs.com',
    'clips.twitch.tv',
)

blacklisted_titles = (
    'nigri',
)


def get_random_media_submission(bot, subreddit_name: str):
    subreddit = bot.reddit.subreddit(subreddit_name)
    site_str = ' OR '.join(accepted_sources)
    results = list(subreddit.search('site:(' + site_str + ')', sort='new', time_filter='month', limit=1000))
    if not results:
        return None
    result = random.choice(results)
    while any(x in result.title.lower() for x in blacklisted_titles):
        result = random.choice(results)
    return result.url


def get_random_submission_by_title(bot, subreddit_name: str, search_str: str):
    results = []
    for result in bot.reddit.subreddit(subreddit_name).search('title:' + search_str):
        results.append(result.permalink)

    logging.debug('subreddit: ' + subreddit_name + ' search string: ' + search_str + ' results length: '
                  + str(len(results)))

    return random.choice(results)
