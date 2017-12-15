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


def beautiful_soup_scraper(html):
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
    for name, scraper in ('Regular expressions', regex_scraper), ('Beautiful Soup', beautiful_soup_scraper), ('Lxml',
                                                                                                              lxml_scraper):
        times[name] = []
        # record the start time of scraper
        start = time.time()
        for i in range(NUM_ITERATIONS):
            if scraper == regex_scraper:
                re.pruge()
            result = scraper(html)

            assert(result['area'] == '1,580 square kilometres')
            times[name].append(time.time() - start)
    end = time.time()
    print '{}: {:.2f} seconds'.format(name, end - start)


writer = csv.writer(open('times.csv', 'w'))
header = sorted(times.keys())
writer.writerow(header)
for row in zip(*[times[scraper] for scraper in header]):
    write.writerow(row)


if __name__ == '__main__':
    main()
