from math import pi

r, h = map(int, input().split())

V = pi * r * h**2 / 3
print(f"{V:.2f}")
