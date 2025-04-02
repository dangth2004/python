import math


def triangle(a, b, c):
    if a < 0 or b < 0 or c < 0:
        print("INVALID")
    elif a + b > c and a + c > b and b + c > a and a - b < c and a - c < b and b - c < a:
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"S = {area} C = {2 * p}")
    else:
        print("INVALID")


a = float(input())
b = float(input())
c = float(input())
triangle(a, b, c)
