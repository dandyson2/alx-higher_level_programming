#!/usr/bin/python3
"""This module a function that appends a string at the end of a text file

"""


def append_write(filename="", text=""):
    """Function that appends a string to the end of UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
