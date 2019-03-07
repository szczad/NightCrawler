#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 03.03.19 17:09

import sys

if sys.version_info < (3, ):
    from urlparse import urlparse
else:
    from urllib.parse import urlparse

import unittest

from nightcrawler.matchers import AnchorMatcher


class AnchorMatcherTest(unittest.TestCase):
    def test_match_with_list(self):
        test_html = """
    <html>
    <head>
        <title>Test title</title>
    </head>
    <body>
        <div>
            some text
            <a href="https://www.google.com/">Google search engine</a>
            <a href="https://www.google.com/">Google search engine</a>
            another text
            <p>A paragraph</p>
            <span><a href="https://www.onet.pl/">Onet portal</a></span>
        </div>
    </body>
    </html>    
    """
        url = urlparse('http://www.google.com/')

        matcher = AnchorMatcher(list_class=list)
        internal, external = matcher.parse(test_html, url)

        self.assertEqual(len(internal), 2)
        self.assertEqual(len(external), 1)

        self.assertEqual(internal[0].geturl(),  "https://www.google.com/")
        self.assertEqual(internal[1].geturl(),  "https://www.google.com/")

        self.assertEqual(external[0].geturl(),  "https://www.onet.pl/")
