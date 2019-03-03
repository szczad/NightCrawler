#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 02.03.19 22:33


class ElasticList(object):
    def __init__(self):
        self._queue = []
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
    def __init__(self):
        super().__init__()

    def push(self, item):
        if item not in self._queue:
            self._queue.append(item)
    append = push
