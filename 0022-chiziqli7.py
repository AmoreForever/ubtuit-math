from math import *

input_values = input().split()

x1, x2 = map(float, input_values[:2])
c, d = map(int, input_values[2:])

F = (
    (
        abs(
            (
                sin((abs(c * x2**3 + d * x1**3 - c * d))) ** 2
                / sqrt(c * x1**2 + d * x2**2 + 7)
            )
        )
    )
) + tan(x1 * x2**2 + d**3)

print(f"{F:.2f}")
