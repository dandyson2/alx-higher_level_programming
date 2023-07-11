#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Checks if object is an instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if object is an instance of the class, False otherwise.
    """
    return obj.__class__ == a_class
