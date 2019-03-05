#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 03.03.19 17:09

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
        matcher = AnchorMatcher(list_class=list)
        results = matcher.parse(test_html)

        self.assertEqual(len(results), 3)

        self.assertEqual(results[0].url,  "https://www.google.com/")
        self.assertEqual(results[1].url,  "https://www.google.com/")
        self.assertEqual(results[2].url,  "https://www.onet.pl/")
