#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    return add(add(a, b), sum(range(4, 6))) if a < b else sub(a, b)
