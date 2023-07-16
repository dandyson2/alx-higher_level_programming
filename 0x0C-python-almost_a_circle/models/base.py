#!/usr/bin/python3
"""This module defines a base class"""


import json
import csv
import turtle


class Base:
    """Base class for managing id attribute."""

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base object.

        Args:
            id (int, optional): ID value for the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            # Increment __nb_objects and assign the new value to id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the string "[]" if list_dic is None or empty, otherwise JSON

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
