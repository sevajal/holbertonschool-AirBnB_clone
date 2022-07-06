#!/usr/bin/python3

"""Unittest for City Class"""

import unittest
from models.city import City

class Test_base(unittest.TestCase):
    """Class Test for City"""

    def test_uuid(self):
        c1 = City()
        c2 = City()
        self.assertIsInstance(c1, City)
        self.assertTrue(hasattr(c1, "id"))
        self.assertNotEqual(c1.id, c2.id)
        self.assertIsInstance(c1.id, str)

if __name__ == '__main__':
    unittest.main()