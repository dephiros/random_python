#!/usr/bin/env python3
# -*- coding: utf8 -*-
class LinkedList(object):
    class Node(object):
        def __init__(self, value, node=None):
            self.value = value
            self.next = node

    def __init__(self, head=None):
        self.head = head
        self.tail = head


    def append(self, value):
        new_node = self.Node(value)
        if not self.head: self.head = new_node
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node

    def __str__(self):
        result = ''
        current = self.head
        while(current):
            result += "{:d} -> ".format(current.value)
            current = current.next
        return result

l = LinkedList()
for i in range(20):
    l.append(i)
print(l)
