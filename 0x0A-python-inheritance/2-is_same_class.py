#!/usr/bin/python3
"""Checks if object is an instance of a class.

"""
def is_same_class(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if object is an instance of the class, False otherwise.
    """
    return (type(obj) == a_class)
