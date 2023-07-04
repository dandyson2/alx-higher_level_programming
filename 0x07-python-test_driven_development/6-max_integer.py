#!/usr/bin/python3
"""The module contains a function that finds the max integer in a list

"""


def max_integer(lst=[]):
    """Find the maximum integer in a list.

    Args:
        lst (list): The list of integers.

    Returns:
        int: The maximum integer in the list. Return None if the list is empty

    """
    if len(lst) == 0:
        return None
    result = lst[0]
    for num in lst[1:]:
        if num > result:
            result = num
    return result
