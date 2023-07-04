#!/usr/bin/python3
"""The module of a function that adds two numbers

"""


def add_integer(a, b=98):
    """Add two numbers and return the result.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Default is 98.

    Returns:
        int: The addition of the two given numbers.

    Raises:
        TypeError: If a or b are not integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float.")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float.")

    a = int(a)
    b = int(b)
    return a + b
