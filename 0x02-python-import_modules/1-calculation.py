#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5

addition = add(a, b)
subtraction = sub(a, b)
multiplication = mul(a, b)
divide = div(a, b)

print("{} + {} = {}".format(a, b, addition))
print("{} - {} = {}".format(a, b, subtraction))
print("{} * {} = {}".format(a, b, multiplication))
print("{} / {} = {}".format(a, b, divide))
