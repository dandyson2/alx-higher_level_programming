#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[(lambda x: x ** 2)(element) for element in row] for row in matrix]
