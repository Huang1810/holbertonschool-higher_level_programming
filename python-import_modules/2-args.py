#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, 's' if argc != 1 else ''))
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
