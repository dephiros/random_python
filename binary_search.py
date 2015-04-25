import unittest

def binary_search(things, thing):
    low, high = 0, len(things) - 1
    while low <= high:
        mid = (high + low) / 2
        if thing == things[mid]:
            return mid
        elif thing < things[mid]:
            high = mid - 1
        else:
            low = mid + 1

class BinarySearchTest(unittest.TestCase):

    def test_not_found(self):
        self.assertIsNone(binary_search([2, 3, 4, 5], 0))

    def test_found_begin(self):
        self.assertEqual(binary_search([2, 3, 4, 5], 2), 0)

    def test_found_end(self):
        self.assertEqual(binary_search([2, 3, 4, 5], 5), 3)

if __name__ == '__main__':
    unittest.main()

