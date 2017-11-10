""" bot.py

Contains the SnackBot class
"""

import sys
import traceback
from discord.ext.commands import Bot

initial_extensions = (
    'discord_client.cogs.reddit',
    'discord_client.cogs.misc',
    'discord_client.cogs.rng',
)


class SnackBot(Bot):
    def __init__(self, reddit, prefix):
        super().__init__(command_prefix=prefix, description='SnackBot by bsnackin#3818', pm_help=True)
        self.reddit = reddit

    async def on_ready(self):
        print('---------------------')
        print('Logged in as ' + self.user.name)
        print('---------------------')

        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()
