from math import *

x, y = map(float, input().split())

c1 = (x + y) / (y**2 + abs((y**2 + 2) / (x + (x**3 / 5)))) + e ** (y + 2)

print(f"{c1:.2f}")
