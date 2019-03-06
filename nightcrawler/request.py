#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 02.03.19 18:21

import requests

from nightcrawler import user_agent, logger
from nightcrawler.matchers import AnchorMatcher
from nightcrawler.utils import UniqueElasticList

matcher = AnchorMatcher()


class PageCrawler(object):
    log = logger.getLogger('request.PageCrawler')

    def __init__(self, url):
        self.__domain = url.netloc
        self.__queue = UniqueElasticList(url)
        self.__visited_urls = UniqueElasticList()

    def process(self):
        for url in self.__queue:
            self.__process(url)
        return self.__visited_urls[:]

    def __process(self, url):
        if url.netloc != self.__domain:
            return

        req = Request(url)
        for result in req.get_links():
            if result in self.__visited_urls:
                continue

            self.__queue.append(result)
        self.__visited_urls.append(url)


class Request(object):
    log = logger.getLogger('request.HTTPRequest')
    headers = {
        'user-agent': user_agent
    }

    def __init__(self, url):
        self.__url = url

    def get_links(self):
        self.log.debug("Making request to: %s" % self.__url.geturl())
        content = requests.get(self.__url.geturl(), headers=self.headers)
        return matcher.parse(content.text, self.__url) if content.status_code == 200 else []
