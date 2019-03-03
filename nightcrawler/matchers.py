#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 02.03.19 20:57
import datetime

from bs4 import BeautifulSoup

from nightcrawler import logger
from nightcrawler.results import Page


class BaseMatcher(object):
    def parse(self, content):
        raise NotImplementedError("Not implemented in base class")


class AnchorMatcher(BaseMatcher):
    def parse(self, content):
        results = []

        log = logger.getLogger('matchers.AnchorMatcher')
        log.debug("Parsing content")

        parser = BeautifulSoup(content, "html.parser")
        for item in parser.find_all("a"):
            date = datetime.datetime.now()
            href = item.get('href')
            results.append(Page(_url=href, _modified=date))

            log.debug('Found url: {url}'.format(url=href))

        return results


if __name__ == "__main__":
    _log = logger.getLogger('')
    _log.setLevel(logger.DEBUG)
    _log.info("Starting unit test")
    test_html = """
<html>
<head>
    <title>Test title</title>
</head>
<body>
    <div>
        some text
        <a href="https://www.google.com/">Google search engine</a>
        another text
        <p>A paragraph</p>
        <span><a href="https://www.onet.pl/">Onet portal</a></span>
    </div>
</body>
</html>    
"""
    a_matcher = AnchorMatcher()
    results = a_matcher.parse(test_html)

    assert len(results) == 2

    assert results[0].type == "a"
    assert results[0].name == "Google search engine"
    assert results[0].value == "https://www.google.com/"

    assert results[1].type == "a"
    assert results[1].name == "Onet portal"
    assert results[1].value == "https://www.onet.pl/"

    _log.info("Test passed!")

