#!/usr/bin/python3
"""
This module returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    This function looks up all attributes and methods of an object
    and returns them as a list
    """
    return dir(obj)
