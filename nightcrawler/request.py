#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 02.03.19 18:21

import requests

from nightcrawler import user_agent, logger
from nightcrawler.matchers import AnchorMatcher
from nightcrawler.results import Page

matcher = AnchorMatcher()


class PageCrawler(object):
    log = logger.getLogger('request.PageCrawler')

    def __init__(self, url):
        self.__queue = []
        self.__visited_urls = []
        self.__url = Page(url)

    def process(self):
        self.__process(self.__url)
        return self.__visited_urls[:]

    def __process(self, page):
        req = Request(self.normalize_url(page.url))
        for result in req.get_links():
            if result in self.__visited_urls or result in self.__queue:
                continue

            self.__queue.append(result)

        self.__visited_urls.append(page)

    def normalize_url(self, url):
        return url.split('#')[0]


class Request(object):
    log = logger.getLogger('request.HTTPRequest')
    headers = {
        'user-agent': user_agent
    }

    def __init__(self, url):
        self.__url = url

    def get_links(self):
        self.log.debug("Making request to: %s" % self.__url)
        content = requests.get(self.__url, headers=self.headers)
        return matcher.parse(content.text) if content.status_code == 200 else []
