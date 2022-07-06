#!/usr/bin/python3

"""Unittest for Amenity Class"""

import unittest
from models.amenity import Amenity

class Test_base(unittest.TestCase):
    """Class Test for Amenity"""

    def test_uuid(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertIsInstance(am1, Amenity)
        self.assertTrue(hasattr(am1, "id"))
        self.assertNotEqual(am1.id, am2.id)
        self.assertIsInstance(am1.id, str)

if __name__ == '__main__':
    unittest.main()