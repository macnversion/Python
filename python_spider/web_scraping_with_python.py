# -*- coding: utf-8 -*-
# 用python写网络爬虫
# %% 使用的库
import urllib2
import re
import itertools
import builtwith
import whois
import urlparse
import robotparser
import datetime

# %% 爬虫
url = r'http://example.webscraping.com/'

# 查看网站所所使用的技术和所有者
builtwith.parse(url)
whois.whois(url)


def download(url, user_agent='wswp', proxy = None, num_retries=2):
    print 'Downloading url:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)

    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
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
    # keep track which url has been seen before
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        user_agent = 'BadCrawler'
        rp = robotparser.RobotFileParser()
        rp.set_url(url + '/robot.txt')
        if rp.can_fetch(user_agent, url):
            for link in get_links(html):
                if re.match(link_regex, link):
                    link = urlparse.urljoin(seed_url, link)
                    if link not in seen:
                        seen.add(link)
                        crawl_queue.append(link)
        else:
            print 'Blocked by robots.txt:', url
    return crawl_queue


def get_links(html):
    '''return a list of links from html'''
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)

class Throttle:
    '''Add a delay between downloads to the same domain'''

    def __init__(self, delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        domian = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                # domain has been accessed recently
                # so need to sleep
                time.sleep(sleep_secs)

        self.domains[domian] = datetime.datetime.now()


# %% 数据抓取
 url = r'http://example.webscraping.com/places/default/view/239'
 html = download(url)
 result = re.findall('<td class="w2p_fw">(.*?)</td>', html)