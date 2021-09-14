
def fibonacci(n) :
    a = 0
    b = 1
    if n < 0 :
        print('incorrect input')
    elif n == 0 :
        return 0
    elif n == 1 :
        return b
    else:
        for i in range(1, n) :
            c = a + b
            a = b
            b = c
        return b
o = list(range(1,34))
list = [fibonacci(element) for element in o]
even_fibonacci = [n for n in list if n % 2 == 0]
print(even_fibonacci)
sum_fibonacci = sum(even_fibonacci)

print(sum_fibonacci)

