import math

a = -0.9
b = -0.4
h = 0.05

x = a
while x <= b + 1e-9:
    if x <= -0.7:
        y = math.atan(x**3)
    elif -0.7 < x <= -0.6:  
        y = math.tan(x + math.log(abs(x)))
    else:
        y = 1 / math.tan(x**2)

    print(f"x = {x:.2f}, f(x) = {y:.6f}")
    x += h

x = x + h 