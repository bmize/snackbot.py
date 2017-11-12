""" wikipedia.py

Functions for grabbing data from wikipedia articles
"""

from bs4 import BeautifulSoup
import random
import re
from urllib import request

BASE_WIKI_URL = 'https://en.wikipedia.org'


def get_snack():
    """Scrapes a list of snack foods and randomly selects one"""
    html = request.urlopen(BASE_WIKI_URL + '/wiki/List_of_snack_foods').read()
    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify()

    tables = soup.find_all('table')
    results = []

    for table in tables:
        tr_list = table.find_all('tr')

        for tr in tr_list:
            td_list = tr.find_all('td')

            if td_list:
                hrefs = td_list[0].find_all('a')
                href = None

                if hrefs:
                    href = hrefs[0].get('href')
                    if '#cite ' in href:
                        href = None

                text = td_list[0].text
                regex = re.compile('[\[\]0-9]')
                text = regex.sub('', text).rstrip()

                if text == 'Portals\nAccess related topics':
                    return random.choice(results)

                if href is None:
                    results.append((text, href))
                else:
                    results.append((text, BASE_WIKI_URL + href))

    return random.choice(results)
