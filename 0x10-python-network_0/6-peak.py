#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(input_list):
    """
    Args:
        input_list(list): list of integers to find peak of
    Returns: peak of input_list or None
    """
    size = len(input_list)

    if size == 0:
        return None

    mid = size // 2

    for _ in range(size):
        mid_e = mid // 2

        if (mid < size - 1 and input_list[mid] < input_list[mid + 1]):
            mid += mid_e if mid_e != 0 else 2
        elif mid_e > 0 and input_list[mid] < input_list[mid - 1]:
            mid -= mid_e if mid_e != 0 else 2
        else:
            return input_list[mid]
