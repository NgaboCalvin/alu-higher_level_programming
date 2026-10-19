#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print(sum(int(argument) for argument in sys.argv[1:]))
