from math import sqrt

MAX = 100000

prime = [True for i in range(MAX + 1)]

def sieve():
    k = int(sqrt(MAX))
    for p in range(2, k, 1):
        if (prime[p] == True):
            for i in range(p * 2, MAX, p):
                prime[i] = False

def divCount(n):
    total = 1
    for p in range(2, n + 1, 1):
        if (prime[p]):
            count = 0
            if (n % p == 0):
                while (n % p == 0):
                    n = n / p
                    count += 1

                total = total * (count + 1)

    return total

def findNumber(n):
    if (n == 1):
        return 3

    i = 2

    count = 0

    second = 1
    first = 1

    while (count <= n):
        if (i % 2 == 0):
            first = divCount(i + 1)

            count = first * second


        else:
            second = divCount(int((i + 1) / 2))

            count = first * second

        i += 1
    return i * (i - 1) / 2


if __name__ == '__main__':
    n = 4

    sieve()
    print(int(findNumber(500)))

