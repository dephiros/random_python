#!/usr/bin/env python3

# The Utopian Tree goes through 2 cycles of growth every year. The first growth cycle occurs during the spring, when it doubles in height. The second growth cycle occurs during the summer, when its height increases by 1 meter.
# Now, a new Utopian Tree sapling is planted at the onset of spring. Its height is 1 meter. Can you find the height of the tree after N growth cycles?
import unittest

def utopia_tree_height(cycles, init_height=1):

    def spring_grow(height):
        return height * 2

    def summer_grow(height):
        return height + 1

    is_spring = True
    for i in range(cycles):
        if is_spring: init_height = spring_grow(init_height)
        else: init_height = summer_grow(init_height)
        is_spring = not is_spring
    return init_height

class TestUtopiaTree(unittest.TestCase):
    def test_0_cycle(self):
        self.assertEqual(utopia_tree_height(0), 1)

    def test_1_cycle(self):
        self.assertEqual(utopia_tree_height(1), 2)

    def test_4_cycle(self):
        self.assertEqual(utopia_tree_height(4), 7)

if __name__ == '__main__':
    unittest.main()


