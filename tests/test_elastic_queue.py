#!/bin/env python
# -*- coding: utf-8 -*-

# Author: Grzegorz Szczudlik
# Date: 03.03.19 16:03

import unittest

from nightcrawler.utils import ElasticList, UniqueElasticList


class ElasticListTest(unittest.TestCase):
    def setUp(self):
        self.elastic_list = ElasticList()
        self.elastic_list.push('F')
        self.elastic_list.push('E')
        self.elastic_list.push('X')
        self.elastic_list.push('E')

    def test_add_elements(self):
        self.assertEqual(self.elastic_list.values(), ['F', 'E', 'X', 'E'])

    def test_remove_elements(self):
        self.assertEqual(self.elastic_list.pop(), 'F')
        self.assertEqual(self.elastic_list.values(), ['E', 'X', 'E'])

    def test_iteration(self):
        result = [i for i in self.elastic_list]
        self.assertEqual(result, ['F', 'E', 'X', 'E'])

    def test_enhanced_iteration(self):
        self.elastic_list.__iter__()

        next1 = self.elastic_list.__next__()
        next2 = self.elastic_list.__next__()

        pop1 = self.elastic_list.pop()
        self.elastic_list.push('T')

        next3 = self.elastic_list.__next__()
        next4 = self.elastic_list.__next__()
        next5 = self.elastic_list.__next__()

        self.assertRaises(StopIteration, self.elastic_list.__next__)
        self.assertEqual(next1, 'F')
        self.assertEqual(next2, 'E')
        self.assertEqual(next3, 'X')
        self.assertEqual(next4, 'E')
        self.assertEqual(next5, 'T')
        self.assertEqual(pop1, 'F')
        self.assertEqual(len(self.elastic_list), 4)


class UniqueElasticQueueTest(unittest.TestCase):
    def setUp(self):
        self.elastic_list = UniqueElasticList()
        self.elastic_list.push('F')
        self.elastic_list.push('E')
        self.elastic_list.push('X')
        self.elastic_list.push('E')

    def test_add_elements(self):
        self.assertEqual(self.elastic_list.values(), ['F', 'E', 'X'])
