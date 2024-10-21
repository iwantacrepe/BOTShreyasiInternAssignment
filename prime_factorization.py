def prime_factorization(n):
    factors = []

    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        factors.append((2, count))

    for i in range(3, int(n**0.5) + 1, 2):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            factors.append((i, count))

    if n > 2:
        factors.append((n, 1))

    return factors


print(prime_factorization(60))
