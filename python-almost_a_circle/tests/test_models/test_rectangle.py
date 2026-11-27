#!/usr/bin/python3
"""Tests for Rectangle class."""
import unittest
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.x = {}

    def test_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_to_dict_and_create(self):
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        r2 = Rectangle.create(**d)
        self.assertEqual(str(r2), str(r))
        self.assertIsNot(r, r2)

    def test_save_load(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertEqual(len(out), 2)
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
