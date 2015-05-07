#!/usr/bin/env python3
# -*- coding: utf8 -*-
import random
import copy

class LinkedList(object):
    class Node(object):
        def __init__(self, value, node=None, random_node=None):
            self.value = value
            self.next = node
            self.random_node = random_node

        def __str__(self):
            return "{}(->{})".format(self.value, str(self.random_node))

        def __deepcopy__(self, memo):
            return self.__class__(self.value)

    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.count = 0

    def get(self, index):
        current = self.head
        while(index > 0 and current):
            current = current.next
            index -= 1
        return current

    def get_random_node(self):
        index = random.randrange(0, self.count + 1)
        return self.get(index)

    def append(self, value, set_random_node=True):
        random_node = self.get_random_node() if set_random_node else None
        new_node = value if isinstance(value, self.Node) else self.Node(value, random_node=random_node)
        self.count += 1
        if not self.head: self.head = new_node
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node

    def __len__(self):
        return self.count

    def __str__(self):
        result = ''
        current = self.head
        while(current):
            result += "{:s} -> ".format(str(current))
            current = current.next
        return result

    def __deepcopy__(self, memo):
        current = self.head
        new_l = self.__class__()
        hash_table = {} # use for quick access to build random node link
        while(current):
            new_node = copy.deepcopy(current) # this will only copy the value and not the link
            hash_table[current] = new_node
            print(current, new_node)
            new_l.append(new_node, set_random_node=False)
            current = current.next
        # now set the random link
        print(self)
        print(new_l)
        current = self.head
        new_current = new_l.head
        while(current):
            if current.random_node: print(hash_table[current.random_node])
            if current.random_node: new_current.random_node = hash_table[current.random_node]
            current = current.next
            new_current = new_current.next
        return new_l

l = LinkedList()
for i in range(20):
    l.append(i)
copied_l = copy.deepcopy(l)
print(l)
print(copied_l)
current = l.head
ccurrent = copied_l.head
checked = True
while(current):
    checked = checked and (current is not ccurrent)
    current = current.next
print(checked)
