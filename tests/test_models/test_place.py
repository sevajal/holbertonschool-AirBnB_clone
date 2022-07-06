#!/usr/bin/python3

"""Unittest for Place Class"""

import unittest
from models.place import Place
from models.base_model import BaseModel

class Test_base(unittest.TestCase):
    """Class Test for Place"""

    def test_uuid(self):
        p1 = Place()
        p2 = Place()
        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "id"))
        self.assertNotEqual(p1.id, p2.id)
        self.assertIsInstance(p1.id, str)

    def test_is_subclass(self):
        p1 = Place()
        self.assertIsInstance(p1, BaseModel)
        
    def test_datetime(self):
        p1 = Place()
        self.assertTrue(hasattr(p1, "created_at"))
        self.assertTrue(hasattr(p1, "updated_at"))
        self.assertNotEqual(p1.created_at, p1.updated_at)

    def test_attributes(self):
        p1 = Place()
        self.assertTrue(hasattr(p1, "name"))
        self.assertEqual(p1.name, "")
        self.assertIsInstance(p1.name, str)
        self.assertTrue(hasattr(p1, "city_id"))
        self.assertEqual(p1.city_id, "")
        self.assertIsInstance(p1.city_id, str)
        self.assertTrue(hasattr(p1, "user_id"))
        self.assertEqual(p1.user_id, "")
        self.assertIsInstance(p1.user_id, str)
        self.assertTrue(hasattr(p1, "description"))
        self.assertEqual(p1.description, "")
        self.assertIsInstance(p1.description, str)
        self.assertTrue(hasattr(p1, "number_rooms"))
        self.assertEqual(p1.number_rooms, 0)
        self.assertIsInstance(p1.number_rooms, int)
        self.assertTrue(hasattr(p1, "number_bathrooms"))
        self.assertEqual(p1.number_bathrooms, 0)
        self.assertIsInstance(p1.number_bathrooms, int)
        self.assertTrue(hasattr(p1, "max_guest"))
        self.assertEqual(p1.max_guest, 0)
        self.assertIsInstance(p1.max_guest, int)
        self.assertTrue(hasattr(p1, "price_by_night"))
        self.assertEqual(p1.price_by_night, 0)
        self.assertIsInstance(p1.price_by_night, int)
        self.assertTrue(hasattr(p1, "latitude"))
        self.assertEqual(p1.latitude, 0.0)
        self.assertIsInstance(p1.latitude, float)
        self.assertTrue(hasattr(p1, "longitude"))
        self.assertEqual(p1.longitude, 0.0)
        self.assertIsInstance(p1.longitude, float)
        self.assertTrue(hasattr(p1, "amenity_ids"))
        self.assertEqual(p1.amenity_ids, [])
        self.assertIsInstance(p1.amenity_ids, list)

    def test_add_attributes(self):
        p1 = Place()
        p1.email = "Sebas@holberton.com"
        p1.number = 90
        self.assertTrue(hasattr(p1, "email"))
        self.assertEqual(p1.email, "Sebas@holberton.com")
        self.assertIsInstance(p1.email, str)
        self.assertTrue(hasattr(p1, "number"))
        self.assertEqual(p1.number, 90)
        self.assertIsInstance(p1.number, int)

    """def test_module_docstring(self):
        self.assertNotEqual(print(__import__("place").__doc__), "")

    def test_class_docstring(self):
        self.assertNotEqual(print(__import__("place").Place.__doc__), "")"""

if __name__ == '__main__':
    unittest.main()