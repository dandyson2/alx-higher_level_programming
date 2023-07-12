#!/usr/bin/python3
"""Module that adds all arguments to a Python list and save them to a file.

"""


import sys


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON format"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file"""
    with open(filename) as file:

        return json.load(file)


if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
