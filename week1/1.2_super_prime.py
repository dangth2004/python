import math


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def is_super_prime(number):
    if number == 0:
        return False
    while number > 1:
        if not is_prime(number):
            return False
        number = number // 10
    return True


number = int(input())
print(is_super_prime(number))
