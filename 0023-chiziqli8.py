from math import *

input_values = input().split()

a, b, c, d = map(int, input_values[:4])
x = float(input_values[4])

try:
    y2 = ((a * x**2 + b * x + c) / (x * a**3 + a**2 + a ** (b - c))) + cos(
        abs(((a * x + b) / (c * x + d + 2**c)))
    )
except ZeroDivisionError:
    y2 = 1

print(f"{y2:.2f}")
