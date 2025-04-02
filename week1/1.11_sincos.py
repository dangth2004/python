import math


def sinTaylor(x, terms=10):
    result = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        result += term
    return result


def cosTaylor(x, terms=10):
    result = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        result += term
    return result
