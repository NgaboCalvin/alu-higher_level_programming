#!/usr/bin/python3
for first in range(0, 9):
    for second in range(first + 1, 10):
        print("{:02d}".format(first * 10 + second),
              end='\n' if second == 9 and first == 8 else ", ")
