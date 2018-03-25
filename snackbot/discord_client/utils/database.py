""" database.py

Functions for connecting to and interacting with a PostgreSQL database
"""

import os
import psycopg2
from psycopg2 import sql


def select_query(query):
    """Queries the database (stored in the OS environment as 'DATABASE_URL') with the provided query

    :param query: string representing a postgreSQL select query (e.g. SELECT * FROM snacks LIMIT 1)
    :return: tuple representing row(s) returned from executing the query
    """
    conn = None
    result = None

    try:
        conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')
        cur = conn.cursor()
        cur.execute(sql.SQL(query))
        result = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return result
