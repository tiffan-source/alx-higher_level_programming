#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest


class Rectangle_Test(unittest.TestCase):

    def setUp(self):
        self.obj = Rectangle(20, 30, 1, 5, 100)
        self.not_init = Rectangle(90, 90, 1, 1)

    def tearDown(self):
        del self.obj
        del self.not_init

    def test_attribute_x_not_init(self):
        data = Rectangle(12, 12)
        self.assertEqual(data.x, 0)

    def test_attribute_y_not_init(self):
        data = Rectangle(12, 12)
        self.assertEqual(data.y, 0)

    def test_Rectangle_doc(self):
        self.assertIsNotNone(Rectangle.__doc__)

    def test_module_doc(self):
        import models.rectangle
        self.assertIsNotNone(models.rectangle.__doc__)

    def test_init_doc(self):
        self.assertIsNotNone(Rectangle.__init__)

    def test_attribute_height(self):
        self.assertEqual(self.obj.height, 30)
        self.obj.height = 100
        self.assertEqual(self.obj.height, 100)

    def test_attribute_width(self):
        self.assertEqual(self.obj.width, 20)
        self.obj.width = 21
        self.assertEqual(self.obj.width, 21)

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
