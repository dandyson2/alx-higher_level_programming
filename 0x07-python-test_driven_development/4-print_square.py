#!/usr/bin/python3
"""The module contains a function that prints a square with the character #

"""


def print_square(size):
    """Print a square with the character '#' of the given size.

    Args:
        size (int): The size of the square.

    Returns:
        None

    Raises:
        TypeError: If size is not an integer number.
        ValueError: If size is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    i = 0
    while i < size:
        print("#" * size)
        i += 1
