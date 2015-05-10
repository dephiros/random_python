#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import random

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or self.min_stack[-1] > value:
            self.min_stack.append(value)

    def pop(self):
        if self.stack:
            value = self.stack.pop()
            if not value > self.min_stack[-1]:
                self.min_stack.pop()
            return value

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]

class TestMinStack(unittest.TestCase):
    def test_empty_stack(self):
        empty_stack = MinStack()
        self.assertIsNone(empty_stack.pop())
        self.assertIsNone(empty_stack.peek())
        self.assertIsNone(empty_stack.get_min())

    def test_push_100(self):
        l = 100
        stack = MinStack()
        values = [random.randint(0,10000) for i in range(l)]
        for v in values:
            stack.push(v)
            self.assertEqual(stack.peek(), v)
        for i in range(l):
            j = l - 1 - i
            self.assertEqual(stack.get_min(), min(values[0:j+1]))
            self.assertEqual(stack.pop(), values[j])

if __name__ == '__main__':
    unittest.main()
