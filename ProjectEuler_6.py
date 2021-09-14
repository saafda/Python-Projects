from time import time
import numpy as np

t0 = time()
list = []
for i in range(1, 10001):
    for n in range(1, 101):
        if i == n**2 :
            list.append(i)
print(sum(list))
dif = (5050**2) - 338350
print(dif)
t = time()
print('Petter\'s trash-ass code:', t - t0)

t0 = time()

N = 100
S2 = 0
for n in range(1, N+1):
    S2 += n**2

print((N*(N+1)//2)**2 - S2)
t = time()
print('Aleks\' chad code:', t - t0)