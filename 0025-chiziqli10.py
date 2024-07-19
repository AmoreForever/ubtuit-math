from math import *

input_values = input().split()

a = int(input_values[0])
x = float(input_values[1])

TT = (
    (sqrt(x - 1) + sqrt(x + 2) + log10(sqrt(a*x**2) + 2)) / 
    (sqrt(sqrt(x+2) + sqrt(x + 24) + x**5))
)

print(f"{TT:.2f}")