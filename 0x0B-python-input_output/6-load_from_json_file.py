#!/usr/bin/python3
"""Module that defines a JSON file-reading function

"""


import json


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file"""
    with open(filename) as file:
        return json.load(file)
