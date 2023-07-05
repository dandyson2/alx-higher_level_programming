#!/usr/bin/python3
"""The module contains a class LockedClass with no class

"""


class LockedClass:
    """This class restricts the creation of attributes to only 'first_name'."""

    __slots__ = ["first_name"]
