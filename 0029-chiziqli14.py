from math import *

input_values = input().split()

a = int(input_values[0])
x, y = map(float, input_values[1:])

TT = (
    sqrt(
        y**2 + e**x + sqrt(
            e**x + (((a) / (x**2 + 2))) + (cos(x)**2) / (sin(x)**2)
        ) + cos(x)**3
    )
)