#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class Test_base(unittest.TestCase):

    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_datetime(self):
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertNotEqual(bm1.created_at, bm1.updated_at)

    def test_add_attributes(self):
        bm1 = BaseModel()
        bm1.name = "Sebas"
        bm1.number = 90
        self.assertTrue(hasattr(bm1, "name"))
        self.assertEqual(bm1.name, "Sebas")
        self.assertIsInstance(bm1.name, str)
        self.assertTrue(hasattr(bm1, "number"))
        self.assertEqual(bm1.number, 90)
        self.assertIsInstance(bm1.number, int)


if __name__ == '__main__':
    unittest.main()
