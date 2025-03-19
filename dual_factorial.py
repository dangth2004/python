def dual_factorial(number):
    result = 1
    while number > 0:
        result *= number
        number -= 2

    return result


number = int(input())
print(f"{number}!! =", dual_factorial(number))
