"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class
    """
    def test_max_integer(self):
        """test max integer
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([-5, -4, -3]), -3)
        self.assertEqual(max_integer([-3, -4, -3]), -3)
        self.assertEqual(max_integer([-3, 50, 99, 11, -3]), 99)

    def test_type(self):
        """test type errors
        """
        self.assertRaises(TypeError, max_integer, [1, "word"])
        self.assertRaises(TypeError, max_integer, [1, [2, 3]])
