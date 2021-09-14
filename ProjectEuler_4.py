
maxx = 0
for i in range(100, 1000) :
    for w in range(100, 1000) :
        x = i * w
        strx = str(x)
        if strx == strx[::-1] and x > maxx :
            maxx = x
            print(x)

