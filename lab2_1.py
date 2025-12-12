import math


a = 1.0
b = 1.5
h = 0.05
eps = 1e-5

x = a

while x <= b + 1e-12: 
    r = 1.0 - 1.0 / x
    s = 0.0
    n = 1
    r_pow = r
    term = r_pow / n

    while abs(term) >= eps:
        s += term
        n += 1
        r_pow *= r
        term = r_pow / n

        if n > 1_000_000:
            break

    ln_x = math.log(x)
    diff = abs(s - ln_x)

    print("x =", round(x, 2),
          "sum =", round(s, 8),
          "ln(x) =", round(ln_x, 8),
          "diff =", "{:.2e}".format(diff),
          "terms =", n - 1)

    x += h
