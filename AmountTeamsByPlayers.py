

for i in range(4, 8):
    t = 0
    for j in range(1, i):
        t += i - j
    print(f'for {i} player there are {t} teams')
