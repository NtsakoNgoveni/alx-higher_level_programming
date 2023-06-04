#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class of testcases for max int """

    def test_ordered(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_unordered(self):
        self.assertEqual(max_integer([2,3,1]), 3)

    def test_start(self):
        self.assertEqual(max_integer([3,1,2]), 3)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        self.assertEqual(max_integer([1]), 1)
        
    def test_float(self):
        self.assertEqual(max_integer([3.8,3.2,3.7]), 3.8)

    def test_mixture(self):
        self.assertEqual(max_integer([-200, 3.56, 10, -10, 10]), 10)

    def test_string(self):
        strings = ["hey","hi","bye"]
        self.assertEqual(max_integer(strings), 'hi')

if __name__ == '__main__':
    unittest.main()
