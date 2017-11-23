# -*- coding: utf-8 -*-


import itertools
from common import download


def iteration():
    max_error = 5
    num_error = 0
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/places/default/view/-{}'.format(page)
        html = download(url)
        if html is None:
            num_error += 1
            if num_error == max_error:
                break
        else:
            num_error = 0


if __name__ == '__main__':
    iteration()
