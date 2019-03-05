#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 05.03.19 22:24

import unittest

from nightcrawler.utils import URL


class URLTest(unittest.TestCase):
    def test_valid_url_no_1(self):
        url = URL('http://valid.tld/')

        self.assertEqual(url.scheme, 'http')
        self.assertEqual(url.domain, 'valid.tld')
        self.assertEqual(url.path, '/')
        self.assertEqual(url.client_url, 'http://valid.tld/')
        self.assertEqual(url.server_url, 'http://valid.tld/')

    def test_valid_url_no_2(self):
        url = URL('http://valid.tld/some_path1/another2')

        self.assertEqual(url.scheme, 'http')
        self.assertEqual(url.domain, 'valid.tld')
        self.assertEqual(url.path, '/some_path1/another2')
        self.assertEqual(url.client_url, 'http://valid.tld/some_path1/another2')
        self.assertEqual(url.server_url, 'http://valid.tld/some_path1/another2')

    def test_valid_url_no_3(self):
        url = URL('http://valid.tld/some_path1/another2?arg1&arg2=val')

        self.assertEqual(url.scheme, 'http')
        self.assertEqual(url.domain, 'valid.tld')
        self.assertEqual(url.path, '/some_path1/another2')
        self.assertEqual(url.arguments, 'arg1&arg2=val')
        self.assertEqual(url.client_url, 'http://valid.tld/some_path1/another2?arg1&arg2=val')
        self.assertEqual(url.server_url, 'http://valid.tld/some_path1/another2?arg1&arg2=val')

    def test_valid_url_no_3(self):
        url = URL('ftp://quite-valid.tld/some_path1/another2?arg1&arg2=val#SomeIdIDontGiveAChance')

        self.assertEqual(url.scheme, 'ftp')
        self.assertEqual(url.domain, 'quite-valid.tld')
        self.assertEqual(url.path, '/some_path1/another2')
        self.assertEqual(url.arguments, 'arg1&arg2=val')
        self.assertEqual(url.fragment, 'SomeIdIDontGiveAChance')
        self.assertEqual(url.client_url, 'ftp://quite-valid.tld/some_path1/another2?arg1&arg2=val#SomeIdIDontGiveAChance')
        self.assertEqual(url.server_url, 'ftp://quite-valid.tld/some_path1/another2?arg1&arg2=val')



