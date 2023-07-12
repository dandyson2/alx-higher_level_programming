#!/usr/bin/python3
"""This module a function that appends a string at the end of a taxt file.

"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF-8 text file"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
