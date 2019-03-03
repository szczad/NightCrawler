#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 02.03.19 19:03


class Page(object):
    def __init__(self, _url, _last_modified=None):
        self._url = _url
        self._last_modified = _last_modified

    @property
    def url(self):
        return self._url

    @property
    def last_modified(self):
        return self._last_modified

    def __hash__(self):
        return hash((self._url, self._last_modified))

    def __eq__(self, other):
        return self._url == other.url \
               and self._last_modified == other.last_modified
