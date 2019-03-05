#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 02.03.19 20:57

import datetime

from bs4 import BeautifulSoup

from nightcrawler import logger
from nightcrawler.utils import UniqueElasticList, URL, InvalidURL


class AnchorMatcher(object):
    def __init__(self, list_class=UniqueElasticList):
        self.__list_cls = list_class

    def parse(self, content, match_domains=[]):
        results = self.__list_cls()

        log = logger.getLogger('matchers.AnchorMatcher')
        log.debug("Parsing content")

        parser = BeautifulSoup(content, "lxml")
        for item in parser.find_all("a"):
            if item is None:
                continue

            try:
                href = URL(item.get('href'))
            except InvalidURL:
                continue

            # Abandon non-HTTP anchors
            if href.scheme not in ('http', 'https'):
                continue

            if match_domains:
                # Stick to specified domains only.
                if href.domain not in match_domains:
                    continue

            results.append(href)
            log.debug('Found url: {url}'.format(url=href))

        return results
