""" snacks.py

Functions relating to snack foods - e.g. getting a random snack from a database
"""

import discord_client.utils.database as db


def get_snack():
    """Queries the database for a random snack

    :return: Tuple representing a snack of the form: (snack name, snack url)
    """
    query = 'SELECT "name", "url" FROM "snacks" ORDER BY RANDOM() LIMIT 1;'
    return db.select_query(query)
