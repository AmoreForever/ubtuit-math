from math import * 

input_values = input().split()

a = int(input_values[0])
x, y = map(float, input_values[1:])

W2 = (
    sqrt(
        e**(x*y) - x * sin(a*x) - (
            (
                x**2 + 2
            ) / (
                abs(x) + 5
            )
        ) 
    ) + 
    sqrt(
        log(x**2+2) + 5
    )
)

print(f"{W2:.2f}")