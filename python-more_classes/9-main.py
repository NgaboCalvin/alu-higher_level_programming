#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
area_val = my_square.area()
perimeter_val = my_square.perimeter()
print("Area: {} - Perimeter: {}".format(area_val, perimeter_val))
print(my_square)
