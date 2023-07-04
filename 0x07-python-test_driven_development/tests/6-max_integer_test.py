#!/usr/bin/python3
"""Unittest for the function def max_integer(list=[])

"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([10, -5, 0, 20, 15]), 20)
        self.assertIsNone(max_integer([]))

        # Add more test cases here...

if __name__ == '__main__':
    unittest.main()
