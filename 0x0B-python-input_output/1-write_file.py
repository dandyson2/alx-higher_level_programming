#!/usr/bin/python3
"""This module a function that writes a string to a text file

"""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns the number of chars"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            num_chars_written = file.write(text)
            return num_chars_written
    except IOError:
        return 0
