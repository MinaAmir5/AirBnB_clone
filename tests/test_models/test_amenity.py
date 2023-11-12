#!/usr/bin/python3
"""
Unitest for amenity.py
"""
import unittest
import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests instnces and methos from amnity class"""

    a = Amenity()

    def testHasAttributes(self):
        """verify if attribtes exist"""
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'updated_at'))
        self.assertTrue(hasattr(self.a, 'name'))

    def test_user_inheritance(self):
        """test if Amenty is a suclass of BaseModel"""
        self.assertIsInstance(self.a, Amenity)

    def test_types(self):
        """tests if the tye of the atribute is the crrect one"""
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)
        self.assertIsInstance(self.a.name, str)

    def test_class_exists(self):
        """tests if class eists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)

if __name__ == '__main__':
    unittest.main()
