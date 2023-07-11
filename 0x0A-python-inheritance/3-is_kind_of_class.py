#!/usr/bin/python3
"""Checks if object is an instance of a class
    or an inherited class.

"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of a class
    or an inherited class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if object is an instance of a specified class, otherwise False.
    """
    return isinstance(obj, a_class)
