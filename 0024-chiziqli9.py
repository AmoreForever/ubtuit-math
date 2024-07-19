from math import *

input_values = input().split()

a, b, c = map(int, input_values[:3])
x = float(input_values[3])

W1 = (
    0.75 + (
        8.2*x **2 + sqrt(abs(x**3 + 3*x) + cos(x - 2))
    ) / (
        (a / 4) + (b / 3) + (c / 2) + 1
    )
)

print(f"{W1:.2f}")