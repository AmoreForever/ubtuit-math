from math import *

x = float(input())

AA = sqrt(((2 * tan(x + 2)) - (cos(x + 2**x))) / (1 + (cos(x + 2)) ** 2)) + (
    sin(x) ** 2
) / (x**2 + 3)


print(f"{AA:.2f}")
