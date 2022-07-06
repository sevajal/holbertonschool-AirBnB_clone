#!/usr/bin/python3

"""Unittest for BaseModel Class"""

import unittest
from models.base_model import BaseModel

class Test_base(unittest.TestCase):
    """Class Test for BaseMmodel"""

    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

if __name__ == '__main__':
    unittest.main()
