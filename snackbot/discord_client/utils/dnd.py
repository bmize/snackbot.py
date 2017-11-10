""" dnd.py

Provides functionality for common DND actions
"""

import random
import re


def roll_dice(num: int, sides: int):
    """Returns a list of rolls"""
    return [str(random.randint(1, sides)) for n in range(num)]


def parse_roll_syntax(die_info: str):
    """Parses a dice roll of format '2d10' into a tuple, e.g. (2, 10)"""
    return map(int, re.findall(r'\d+', die_info))
