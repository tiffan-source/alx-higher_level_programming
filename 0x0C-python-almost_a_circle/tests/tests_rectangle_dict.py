#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class Rectangle_Dic_Test(unittest.TestCase):

    def test_doc_to_dictionary(self):
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test_give_dictionary(self):
        rct = Rectangle(200, 400, 45, 90, 100)
        self.assertTrue(type(rct.to_dictionary()) in [dict])
        self.assertEqual((rct.to_dictionary())["id"], 100)
        self.assertEqual((rct.to_dictionary())["width"], 200)
        self.assertEqual((rct.to_dictionary())["height"], 400)
        self.assertEqual((rct.to_dictionary())["x"], 45)
        self.assertEqual((rct.to_dictionary())["y"], 90)
