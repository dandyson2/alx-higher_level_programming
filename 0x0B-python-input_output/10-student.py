#!/usr/bin/python3
"""Module that defines a text file insertion function

"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student.

        If attrs is a list of strings, only the attributes in the list are rep
        """
        if (
            type(attrs) == list
            and all(type(ele) == str for ele in attrs)
        ):
            return {
                k: getattr(self, k)
                for k in attrs
                if hasattr(self, k)
            }
        return self.__dict__
