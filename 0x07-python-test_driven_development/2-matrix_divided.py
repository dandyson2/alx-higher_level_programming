#!/usr/bin/python3
"""The module contains a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """Divide the numbers in a matrix by a given number.

    Args:
        matrix (list of lists): A matrix represented as a list of lists.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list of lists: A new matrix with the result of the division.

    Raises:
        TypeError: If the matrix elements are not lists, if they are not int,
        if they are not floats
                   If div is not a number.
                   If the rows of the matrix have different sizes.
        ZeroDivisionError: If div is zero.

    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)

        for num in elems:
            if not isinstance(num, (int, float)):
                raise TypeError(msg_type)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return m
