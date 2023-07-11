#!/usr/bin/python3
"""
Checks if an object is an instance of a class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    from the specified class; otherwise, returns False.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
