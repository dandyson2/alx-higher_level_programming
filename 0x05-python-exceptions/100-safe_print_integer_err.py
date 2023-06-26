#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeError):
        print("Exception: Invalid integer value", file=sys.stderr)
        return False
