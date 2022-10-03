#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class Area_Test(unittest.TestCase):

    def test_doc_area(self):
        self.assertIsNotNone(Rectangle.area.__doc__)

    def test_area_value(self):
        rectangle = Rectangle(45, 2, id=90)
        self.assertEqual(rectangle.area(), 90)
        rectangle.width = 100
        self.assertEqual(rectangle.area(), 200)
        rectangle.height = 100
        self.assertEqual(rectangle.area(), 10000)
