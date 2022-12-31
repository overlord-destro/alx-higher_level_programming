#!/usr/bin/python3
"""test file for max_integer function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ class that inherits from testcase class"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_negatives(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_max_zeroes(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_max_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_max_biglist(self):
        self.assertEqual(max_integer([
            32, 44, 4, 20, 68, 27, 36, 69,
            13, 42, 71, 72, 1, 18, 18, 97,
            12, 100, 50, 81, 38, 2, 25, 63,
            54, 15, 68, 75, 76, 86]), 100)

    def test_max_diffdata(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_max_dict(self):
        with self.assertRaises(KeyError):
            max_integer({"1": "2", "2": "4"})

    def test_max_set(self):
        with self.assertRaises(TypeError):
            max_integer({0, 1, 2, 3})
