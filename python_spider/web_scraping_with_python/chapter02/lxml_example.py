#  -*- coding: utf-8 -*-
# example of lxml.html

import urllib2
import lxml.html

def scrape(html):
    tree = lxml.html.fromstring(html)
    td = tree.cssselect('tr#places_neighbours__row > td.w2p_fw')[0]
    area = td.text_content()
    return area


if __name__ == '__main__':
    html = urllib2.urlopen('http://example.webscraping.com/places/default/view/Aland-Islands-2').read()
    print scrape(html)
