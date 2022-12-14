#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class Update_Tests(unittest.TestCase):

    def test_doc_present(self):
        self.assertIsNotNone(Rectangle.update.__doc__)

    def test_no_argument(self):
        rct = Rectangle(200, 300, 25, 65, 90)
        rct.update()
        self.assertEqual(rct.width, 200)
        self.assertEqual(rct.height, 300)
        self.assertEqual(rct.x, 25)
        self.assertEqual(rct.y, 65)
        self.assertEqual(rct.id, 90)

    def test_one_argument(self):
        rct = Rectangle(200, 300, 25, 65, 90)
        rct.update(54)
        self.assertEqual(rct.width, 200)
        self.assertEqual(rct.height, 300)
        self.assertEqual(rct.x, 25)
        self.assertEqual(rct.y, 65)
        self.assertEqual(rct.id, 54)

    def test_one_argument_string(self):
        rct = Rectangle(200, 300, 25, 65, 90)
        rct.update("id")
        self.assertEqual(rct.width, 200)
        self.assertEqual(rct.height, 300)
        self.assertEqual(rct.x, 25)
        self.assertEqual(rct.y, 65)
        self.assertEqual(rct.id, "id")

    def test_two_argument(self):
        rct = Rectangle(200, 300, 25, 65, 90)
        rct.update(90, 1000)
        self.assertEqual(rct.width, 1000)
        self.assertEqual(rct.height, 300)
        self.assertEqual(rct.x, 25)
        self.assertEqual(rct.y, 65)
        self.assertEqual(rct.id, 90)

    def test_two_argument_wrong_second(self):
        rct = Rectangle(200, 300, 25, 65, 90)
        with self.assertRaises(TypeError):
            rct.update(90, "-1000")

    def test_three_argument(self):
        rct = Rectangle(200, 300, 25, 65, 90)
        rct.update(90, 1000, 2000)
        self.assertEqual(rct.width, 1000)
        self.assertEqual(rct.height, 2000)
        self.assertEqual(rct.x, 25)
        self.assertEqual(rct.y, 65)
        self.assertEqual(rct.id, 90)

    def test_four_argument(self):
        rct = Rectangle(200, 300, 25, 65, 90)
        rct.update(90, 1000, 2000, 90)
        self.assertEqual(rct.width, 1000)
        self.assertEqual(rct.height, 2000)
        self.assertEqual(rct.x, 90)
        self.assertEqual(rct.y, 65)
        self.assertEqual(rct.id, 90)

    def test_five_argument(self):
        rct = Rectangle(200, 300, 25, 65, 90)
        rct.update(90, 1000, 2000, 90, 0)
        self.assertEqual(rct.width, 1000)
        self.assertEqual(rct.height, 2000)
        self.assertEqual(rct.x, 90)
        self.assertEqual(rct.y, 0)
        self.assertEqual(rct.id, 90)

    def test_many_arument(self):
        rct = Rectangle(100, 200)
        rct.update(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(rct.width, 2)
        self.assertEqual(rct.height, 3)
        self.assertEqual(rct.x, 4)
        self.assertEqual(rct.y, 5)
        self.assertEqual(rct.id, 1)
