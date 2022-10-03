#!/usr/bin/python3
from models.square import Square
from models.square import Rectangle
import unittest


class Square_Test(unittest.TestCase):

    def setUp(self):
        self.obj = Square(30, 1, 5, 100)

    def test_Square_doc(self):
        self.assertIsNotNone(Square.__doc__)

    def test_module_doc(self):
        import models.square
        self.assertIsNotNone(models.square.__doc__)

    def test_init_doc(self):
        self.assertIsNotNone(Square.__init__.__doc__)

    def test_inherit_from_Rectangle(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_attribute_height(self):
        self.assertEqual(self.obj.height, 30)

    def test_attribute_width(self):
        self.assertEqual(self.obj.width, 30)

    def test_attribute_x(self):
        self.assertEqual(self.obj.x, 1)
        self.obj.x = 218
        self.assertEqual(self.obj.x, 218)

    def test_attribute_y(self):
        self.assertEqual(self.obj.y, 5)
        self.obj.y = 17
        self.assertEqual(self.obj.y, 17)

    def test_id_herit(self):
        self.assertEqual(self.obj.id, 100)

    def test_square_area(self):
        sqrt = Square(100)
        self.assertEqual(sqrt.area(), 10000)

    def test_display_square(self):
        sqrt = Square(34, 89, 90, 120)
        self.assertEqual(str(sqrt), "[Square] (120) 89/90 - 34")
