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
        results[field] = re.search('<tr id="places_{}__row">.*?<td class="w2p_fw">(.*?)</td>'.format(field),
                                   html).groups()[0]
        return results


def beautifuk_soup_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = {}
    for field in fields:
        results[field] = soup.find('table').find('tr', id='places_{}__row'.format(field)).find('td',
                                                                                              class_='w2p_fw').text
        return results


def lxml_scraper(html):
    tree = lxml.html.fromstring(html)
    results = {}
    for field in fields:
        results[field] = tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content()
    return results


def main():
    times = {}
    html = urllib2.urlopen('http://example.webscraping.com/places/default/view/Aland-Islands-2').read()
    NUM_ITERATIONS = 1000 # 每个爬虫测试1000次
