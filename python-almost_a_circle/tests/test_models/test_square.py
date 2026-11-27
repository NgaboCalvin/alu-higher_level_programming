#!/usr/bin/python3
"""Tests for Square class."""
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(Square(5).area(), 25)

    def test_str(self):
        s = Square(10, 2, 1, 5)
        self.assertEqual(str(s), "[Square] (5) 2/1 - 10")

    def test_size(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)
        with self.assertRaises(TypeError):
            s.size = "9"

    def test_update(self):
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")
        s.update(x=12)
        self.assertEqual(s.x, 12)

    def test_to_dict_and_create(self):
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        s2 = Square.create(**d)
        self.assertEqual(str(s2), str(s))

    def test_save_load(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        out = Square.load_from_file()
        self.assertEqual(len(out), 2)
        if os.path.exists("Square.json"):
            os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
