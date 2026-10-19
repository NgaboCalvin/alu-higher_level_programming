#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{}".format(chr(ord(char) - 32))
              if ord(char) >= ord('a') and ord(char) <= ord('z')
              else char, end="")
    print("")
