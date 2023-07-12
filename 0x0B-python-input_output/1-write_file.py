#!/usr/bin/python3
"""This module a function that writes a string to a text file

"""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return f.write(text)
