#!/bin/python3

cache = {"3": 0, "5": 0}
uncount = {}


def submultiples(n):
    for i in range(0, n, 3):  # Get multiples of 3
        cache[3[n]] = i
    for j in range(0, n, 5):  # Get multiples of 5
        cache[n] = j
    for k in range(0, n, 15):  # Remove double-counted multiples of 15
        cache[5[n]] = k
    return (cache)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(submultiples(n))
