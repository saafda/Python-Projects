
for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if a**2 + b**2 == c**2 and a+b+c == 1000:
                print(a, b, c)
#result is a = 200, b = 375, c = 425