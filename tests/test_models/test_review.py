#!/usr/bin/python3

"""Unittest for Review Class"""

import unittest
from models.review import Review

class Test_base(unittest.TestCase):
    """Class Test for Review"""

    def test_uuid(self):
        r1 = Review()
        r2 = Review()
        self.assertIsInstance(r1, Review)
        self.assertTrue(hasattr(r1, "id"))
        self.assertNotEqual(r1.id, r2.id)
        self.assertIsInstance(r1.id, str)

if __name__ == '__main__':
    unittest.main()