#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = len(sys.argv) - 1
    print("{} argument{}:".format(count, "" if count == 1 else "s")
          if count else "0 arguments.")
    for position, argument in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(position, argument))
