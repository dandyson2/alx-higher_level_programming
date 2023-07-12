#!/usr/bin/python3
"""Module that defines a text file insertion function

"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file
    """
    page = ""
    with open(filename) as r:
        for line in r:
            page += line
            if search_string in line:
                page += new_string
    with open(filename, "w") as w:
        w.write(page)
