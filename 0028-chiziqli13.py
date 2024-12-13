from math import *

input_values = input().split()

a = int(input_values[0])
x = float(input_values[1])

BB1 = x * sin((x / 2) + (x / 3) + (x / 4)) + ((log10(x**2 - 2) + 3**a)) / (
    cos(x + 3) * sin(x + 3) + 8
)

print(f"{BB1:.2f}")
