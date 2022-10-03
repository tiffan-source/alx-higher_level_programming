#!/usr/bin/python3
import unittest
from models.base import Base


class Base_Test(unittest.TestCase):

    def test_Base_doc(self):
        self.assertIsNotNone(Base.__doc__)

    def test_module_doc(self):
        import models.base
        self.assertIsNotNone(models.base.__doc__)

    def test_init_doc(self):
        self.assertIsNotNone(Base.__init__)

    def test_private_nb_onjects(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_init_id_with_value(self):
        b = Base(21)
        self.assertEqual(b.id, 21)

    def test_init_id_with_no_value(self):
        b = Base(None)
        self.assertEqual(b.id, 1)
        c = Base(None)
        self.assertEqual(c.id, 2)
        self.assertEqual(b.id, 1)

    def test_init_no_parameter(self):
        a = Base()
        self.assertEqual(a.id, 1)

    def test_init_no_parameter(self):
        a = Base("yo")
        self.assertEqual(a.id, "yo")
