# -*- coding: utf-8 -*-

import itertools
from common import download


def iteration():
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/places/default/view/-{}'.format(page)
        html = download(url)
        if html is None:
            break
        else:
            # success - can scrape the result
            pass


if __name__ == '__main__':
    iteration()
