from math import *

x, y = map(int, input().split())

z = log(
    abs(
        (x + y) ** 2 + sqrt(abs(y) + 2) - (x - (x * y / ((x ** 2 / 2) - 5)))
    )) + ((cos(x + y)) ** 2) / ((x + y) ** (1 / 3))


print(f"{z:.2f}")
