#!/usr/bin/python3
"""Module that defines a class Student"""


class Student:
    """Student representation"""

    def __init__(self, first_name, last_name, age):
        """Initialising a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Acquire a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {s: getattr(self, s) for s in attrs if hasattr(self, s)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        """
        for s, t in json.items():
            setattr(self, s, t)
