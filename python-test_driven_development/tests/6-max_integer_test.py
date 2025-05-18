#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_at_the_end(self):
      self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_the_beginning(self):
       self.assertEqual(max_integer([10, 9, 8, 7]), 10)

    def test_max_in_the_middle(self):
       self.assertEqual(max_integer([100, 200, 300, 250, 50]), 300)

    def test_one_negative_number(self):
       self.assertEqual(max_integer([12, 13, 14, -15]), 14)

    def test_one_element(self):
       self.assertEqual(max_integer([1000]), 1000)

    def test_empty_list(self):
       self.assertIsNone(max_integer(None))

    if __name__ == '__main__':
        unittest.main()
