from math import pi

r1, r2, r3 = map(int, input().split())

area1 = pi * r1**2
area2 = pi * r2**2
area3 = pi * r3**2

print(f"{area1:.2f} {area2:.2f} {area3:.2f}")
