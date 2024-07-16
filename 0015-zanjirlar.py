R1, R2, R3 = map(int, input().split())

r = 1 / (1 / R1 + 1 / R2 + 1 / R3)

print(f"{r:.2f}")
