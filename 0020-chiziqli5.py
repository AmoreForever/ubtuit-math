from math import *

x, y = map(float, input().split())

T11 = (x**2 + 1) / (
    x**2 + ((x * y + y**2) / (y**2 + (y + x * y) / (abs(x * y) + 5)))
) + (1 / (1 + cos(x) + (1 / sin(abs(x)))))

print(f"{T11:.2f}")
