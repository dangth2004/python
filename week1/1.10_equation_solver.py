import numpy as np


# Giải phương trình f(x) = 0 bằng phương pháp chia đôi (đệ quy)
def solver(f, a, b, e=1e-6):
    c = (a + b) / 2
    if np.abs(f(c)) <= e:
        return c
    if f(a) * f(c) < 0:
        return solver(f, a, c, e)
    else:
        return solver(f, c, b, e)
