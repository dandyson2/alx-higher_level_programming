#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

def calculate_result(operator, a, b):
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    return ops[operator](a, b)

if __name__ == "__main__":
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    result = calculate_result(operator, a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
