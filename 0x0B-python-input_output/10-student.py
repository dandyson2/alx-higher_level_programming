#!/usr/bin/python3
"""Module that defines a text file insertion function

"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file"""
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, "w") as file:
        file.writelines(lines)
