import math

for n in range(1, 101):
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    print(*sorted(list(set(d))))
