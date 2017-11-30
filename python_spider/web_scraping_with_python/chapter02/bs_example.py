#  -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup


def scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    tr = soup.find(attrs={'id':'places_area__row'})
    td = tr.find(attrs={'class':'w2p_fw'})
    area = td.text
    return area


if __name__ == '__main__':
    html = urllib2.urlopen('http://example.webscraping.com/places/default/view/Afghanistan-1').read()
    print scrape(html)

