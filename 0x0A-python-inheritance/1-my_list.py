#!/usr/bin/python3
"""This module defines a class that inherits from the list class"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        sorted_list = sorted(self)
        for item in sorted_list:
            print(item)
