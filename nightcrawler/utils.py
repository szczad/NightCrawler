#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 02.03.19 22:33

import re

__all__ = ['ElasticList', 'UniqueElasticList', 'URL', 'InvalidURL']


# This class could implement more magic methods but for given task - it won't unless needed
class ElasticList(object):
    def __init__(self, *args):
        self._queue = []
        self._queue.extend(args)
        self._iter = None

    def push(self, item):
        self._queue.append(item)
    append = push

    def pop(self):
        if self._iter is not None:
            self._iter -= 1
        return self._queue.pop(0)

    def values(self):
        return self._queue[:]

    def __len__(self):
        return len(self._queue)

    def __contains__(self, item):
        return item in self._queue

    def __iter__(self):
        self._iter = 0
        return self

    def __getitem__(self, index):
        return self._queue[index]

    def __next__(self):
        if self._iter is None or len(self._queue)-1 < self._iter:
            self._iter = None
            raise StopIteration()

        value = self._queue[self._iter]
        self._iter += 1
        return value


class UniqueElasticList(ElasticList):
    def __init__(self, *args):
        super().__init__(*args)

    def push(self, item):
        if item not in self._queue:
            self._queue.append(item)
    append = push


class InsensitiveString(str):
    def __init__(self, value):
        super(str).__init__(value)
        self.__value = value

    def __eq__(self, other):
        return self.__value.lower == other.lower()


# Simple yet handy URL decomposer - usable after full URL validation to speed up decomposition
url_re = re.compile(
    r'^(?P<scheme>[^:]+)://'
    r'(?P<domain>[^/]+)'
    r'(?P<path>[^?#]*)'
    r'(?:\??(?P<arguments>[^#]*))'
    r'(?:#?(?P<fragment>.*))$'
)


# Invalid URL Exception - to distinguish URL between validation and other errors
class InvalidURL(Exception):
    pass


# Implementation p2: But this one will - Just for sake of a bit more clarity and testability
class URL(object):
    def __init__(self, url):
        if not url:
            raise InvalidURL('Empty URL provided')

        try:
            match = url_re.match(url)
        except TypeError:
            print("Invalid value found: %s" % url)
            raise

        if not match:
            raise InvalidURL('Invalid URL provided')

        self.__match = match
        self.__url = url

    def __str__(self):
        return self.__url

    def __eq__(self, other):
        return self.server_url == other.server_url

    @property
    def url(self):
        return self.__url

    @property
    def client_url(self):
        return self.__url

    @property
    def server_url(self):
        return "{scheme}://{domain}{path}{arguments}".format(
            scheme=self.scheme,
            domain=self.domain,
            path=self.path or "/",
            arguments="?%s" % self.arguments if self.arguments else ""
        )

    # It is better to interpret results if property is None rather than empty string - None !== False
    @property
    def scheme(self):
        return self.__match.group('scheme').lower() if self.__match.group('scheme') else None

    @property
    def domain(self):
        # IDN domains are case-insensitive
        # SRC: https://stackoverflow.com/questions/7666782/are-idn-domain-names-case-sensitive
        return self.__match.group('domain').lower() or None

    @property
    def path(self):
        return self.__match.group('path') or None

    @property
    def arguments(self):
        return self.__match.group('arguments') or None

    @property
    def fragment(self):
        return self.__match.group('fragment') or None

