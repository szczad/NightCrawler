#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 02.03.19 19:03


class Page(object):
    def __init__(self, _url, _modified=None):
        self._url = _url
        self._modified = _modified

    @property
    def name(self):
        return self._url

    @property
    def value(self):
        return self._modified

    def __hash__(self):
        return hash((self._url, self._modified))

    def __eq__(self, other):
        return self._url == other.name \
               and self._modified == other.value
