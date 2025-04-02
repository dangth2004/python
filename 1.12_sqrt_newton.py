def sqrt_newton(c):
    EPSILON = 1e-15
    t = c
    while abs(t - c / t) > (EPSILON * t):
        t = (t + c / t) / 2
    return t
