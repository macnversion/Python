# -*- coding: utf-8 -*-
# 用python写网络爬虫
# %%
import urllib2
import re
import itertools
import builtwith
import whois

# %%
url = r'http://example.webscraping.com/'

# %% 查看网站所所使用的技术和所有者
builtwith.parse(url)
whois.whois(url)


def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading url:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <= 600:
                # retry 5xx http error
                return download(url, num_retries-1)
    return html

def crawl_sitemap(url):
    # download the sitemap
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*)</loc>', sitemap)
    for link in links:
        html = download(link)

for page in itertools.count(1):
    url = 'http://example.webscraping.com/places/default/view/-%d' % page
    html = download(url)
    if html is None:
        break
    elif page > 5:
        break
    else:
        pass

def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)

        for link in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(link)


def get_links(url):
    '''return a list of links from html'''
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)
