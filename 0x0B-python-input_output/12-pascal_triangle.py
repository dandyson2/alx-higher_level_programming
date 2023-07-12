#!/usr/bin/python3
"""Module that defines a Pascal's Triangle function

"""


def pascal_triangle(n):
    """Function that represents Pascal's Triangle of size n
    """
    if n <= 0:
        return []

    triangles = [[1]]


while len(triangles) != n:
    current_row = triangles[-1]
    next_row = [1]
    i = 0
    while i < len(current_row) - 1:
        next_row.append(current_row[i] + current_row[i + 1])
        i += 1
    next_row.append(1)
    triangles.append(next_row)
return triangles
