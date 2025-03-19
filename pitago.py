import math


def pythagorean_triplets(number):
    for a in range(1, number - 1):
        for b in range(a + 1, number):
            c = math.sqrt(a ** 2 + b ** 2)
            if c > number:
                continue
            if c <= number and c % 1 == 0:
                print(f"({a}, {b}, {int(c)})")


number = int(input())
pythagorean_triplets(number)
