#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)
        
    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_single_element(self):
        self.assertEqual(max_integer([3]), 3)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_float_integers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3, 4])

if __name__ == '__main__':
    unittest.main()
