a, b = map(float, input().split())

T = a ** (1/5) + (b * (a+b)/(2*b + a*b))**(1/4) * (a**2 + b**2 + 2)
print(f"{T:.2f}")
