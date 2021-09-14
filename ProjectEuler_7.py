primes = [2]
n = 3
while len(primes) < 60:
    prime = True
    for p in primes:
        if n % p == 0:
            prime = False
            break
    if prime:
        primes.append(n)
    n += 2

print(primes)
