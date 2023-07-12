#!/usr/bin/python3
"""Module that defines a text file insertion function

"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file"""
    text = ""
    with open(filename) as r:
        line = r.readline()
        while line:
            text += line
            if search_string in line:
                text += new_string
            line = w.readline()
    with open(filename, "w") as w:
        w.write(text)
