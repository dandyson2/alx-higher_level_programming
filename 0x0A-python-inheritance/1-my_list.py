#!/usr/bin/python3
"""This module defines a class that inherits from the list class"""


class MyList(list):
    """
    A class that inherits from the list class.
    Provides an additional method to print a sorted list.
    """

    def print_sorted(self):
        """Prints the elements of the list in sorted order"""
        sorted_list = sorted(self)
        print(sorted_list)
