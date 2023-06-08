#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a, operator, b = map(int, sys.argv[1:4])

ops = {"+": add, "-": sub, "*": mul, "/": div}
if operator not in ops:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

result = ops[operator](a, b)
print(f"{a} {operator} {b} = {result}")

