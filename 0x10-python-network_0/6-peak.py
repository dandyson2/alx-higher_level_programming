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

    start = 0
    end = size - 1

    for _ in range(size):
        mid = (start + end) // 2

        if (mid < size - 1 and
                input_list[mid] < input_list[mid + 1]):
            start = mid + 1
        elif mid > 0 and input_list[mid] < input_list[mid - 1]:
            end = mid - 1
        else:
            return input_list[mid]
