#!/usr/bin/python3
"""This module a function that writes a string to a text file

"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file and returns the number of character

    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
