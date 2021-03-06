# -*- coding utf-8 -*-

import re
from common import download


def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        html = download(link)


if __name__ == '__main__':
    crawl_sitemap('http://example.webscraping.com/sitemap.xml')