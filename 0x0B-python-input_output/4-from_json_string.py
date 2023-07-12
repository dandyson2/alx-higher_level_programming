#!/usr/bin/python3
"""Module that defines a JSON-to-object function

"""


import json


def from_json_string(my_str):
    """Returns the python data structure object represent by a JSON string

    """
    return json.loads(my_str)
