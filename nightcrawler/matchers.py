#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 02.03.19 20:57

import datetime

from bs4 import BeautifulSoup

from nightcrawler import logger
from nightcrawler.page import Page
from nightcrawler.utils import UniqueElasticList


class AnchorMatcher(object):
    def __init__(self, list_class=UniqueElasticList):
        self.__list_cls = list_class

    def parse(self, content):
        results = self.__list_cls()

        log = logger.getLogger('matchers.AnchorMatcher')
        log.debug("Parsing content")

        parser = BeautifulSoup(content, "lxml")
        for item in parser.find_all("a"):
            if item is None:
                continue

            href = item.get('href')
            if href.startswith("#") or not href.startswith(('http://', 'https://')):
                continue

            results.append(Page(url=href, last_modified=datetime.datetime.now()))

            log.debug('Found url: {url}'.format(url=href))

        return results
