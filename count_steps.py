#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

def count_way_n_stairs(n, m=None):
    if m == None: m = [None] * (n + 1)
    if n < 0: return 0
    elif n == 0: return 1
    else:
        if m[n] is None:
            m[n] = count_way_n_stairs(n - 1, m) + count_way_n_stairs(n - 2, m) + count_way_n_stairs(n - 3, m)
        return m[n]

class TestCountNWays(unittest.TestCase):
    def test_count_n_ways_zero(self):
        self.assertEqual(count_way_n_stairs(0), 1)

    def test_count_n_way_3(self):
        self.assertEqual(count_way_n_stairs(3), 4)

    def test_count_n_way_neg(self):
        self.assertEqual(count_way_n_stairs(-1), 0)

if __name__ == '__main__':
    unittest.main()
