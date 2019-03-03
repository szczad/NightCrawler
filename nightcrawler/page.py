#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 02.03.19 19:03


class Page(object):
    def __init__(self, url, last_modified=None):
        self._url = url
        self._last_modified = last_modified

    @property
    def url(self):
        return self._url

    @property
    def last_modified(self):
        return self._last_modified

    def __hash__(self):
        return hash(self._url)

    def __eq__(self, other):
        return self._url == other.url
