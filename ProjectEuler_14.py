import numpy as np

"""def f(n):
    if n % 2 == 0:
        result = n = n//2
    else:
        result = n = 3*n + 1
    return result

def chain_len(n):
    var = f(n)
    lol = [var]
    chain_length = 2
    while var != 1:
        var = f(var)
        chain_length += 1
    return chain_length
max_len = 0
max_n = 0
for n in range(1, 1000000):
    poop = chain_len(n)
    if poop > max_len:
        max_len = poop
        max_n = n
        print(n)"""


chain_lengths = np.zeros(1000001, dtype=int)
chain_lengths[1] = 1
def recur(n):
    if n < 1000001:
        if chain_lengths[n] != 0:
            return chain_lengths[n]
        else:
            if n % 2 == 0:
                chain_lengths[n] = 1 + recur(n//2)
                return chain_lengths[n]
            else:
                chain_lengths[n] = 1 + recur(3*n + 1)
                return chain_lengths[n]
    else:
        if n % 2 == 0:
            return 1 + recur(n//2)
        else:
            return 1 + recur(3*n + 1)


for n in range(1, 1000001):
    print(n, recur(n))

print(np.argmax(chain_lengths))