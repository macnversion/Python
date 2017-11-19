#  -*- coding: utf-8 -*-
# 用python写网络爬虫
# %% 使用的库
import urllib2
import builtwith
import whois
import urlparse

# %% 爬虫
url = r'http://example.webscraping.com'

# 查看网站所所使用的技术和所有者
builtwith.parse(url)
whois.whois(url).__dict__

# 各种不同完整程度的爬虫程序
def download1(url):  # 直接下载网页1
    return urllib2.urlopen(url).read()


def download2(url):  # 处理下载网页失败的情形
    print 'Downloading', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
    return html


def download3(url, num_retries=5):  # 可以重新下载
    print 'Downloading', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download3(url, num_retries-1)
    return  html


def download4(url, user_agent='wswp', num_retries=5):  # 增加user_agent
    print 'Downloading', url
    headers = {'User_agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download4(url ,user_agent, num_retries-1)
    return html


def download5(url, user_agent='wswp', proxy=None, num_retries=2):
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


download = download4()

if __name__ == '__main__':
    print download(url)