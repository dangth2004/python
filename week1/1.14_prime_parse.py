def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 và 1 không phải số nguyên tố
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]


def parse(n):
    if n < 2:
        return f"{n} không hợp lệ"

    primes = sieve(n)
    factors = []
    temp = n

    for p in primes:
        while temp % p == 0:
            factors.append(p)
            temp //= p
        if temp == 1:
            break

    print(f"{n} = " + " x ".join(map(str, factors)))
