#!/usr/bin/python3

"""Unittest for Place Class"""

import unittest
from models.place import Place

class Test_base(unittest.TestCase):
    """Class Test for Place"""

    def test_uuid(self):
        p1 = Place()
        p2 = Place()
        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "id"))
        self.assertNotEqual(p1.id, p2.id)
        self.assertIsInstance(p1.id, str)

if __name__ == '__main__':
    unittest.main()