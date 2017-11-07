import praw
from snackbot import auth


def login():
    return praw.Reddit(client_id=auth.CLIENT_ID, client_secret=auth.CLIENT_SECRET, username=auth.USERNAME,
                       password=auth.PASSWORD, user_agent=auth.USER_AGENT)


if __name__ == '__main__':
    r = login()
    # do cool things
