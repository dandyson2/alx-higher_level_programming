#!/usr/bin/python3
import sys

def print_arguments(count):
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

if __name__ == "__main__":
    count = len(sys.argv) - 1
    print_arguments(count)
