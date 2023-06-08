#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def validate_arguments():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    operator = sys.argv[2]
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    return int(sys.argv[1]), operator, int(sys.argv[3])


def perform_operation(a, operator, b):
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    result = ops[operator](a, b)
    return result


def print_result(a, operator, b, result):
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    a, operator, b = validate_arguments()
    result = perform_operation(a, operator, b)
    print_result(a, operator, b, result)
