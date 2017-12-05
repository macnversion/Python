# -*- coding: utf-8 -*-

import csv
import re
import time
import urllib2
import timeit
import lxml.html
from bs4 import BeautifulSoup

fields = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', 'currency_name',
          'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')


def regex_scraper(html):
    results = {}
    for field in fields:
        results[field] = re.search()