#!/bin/python3

def submultiples(n):
    total = 0
    for i in range(0, n, 3):  # Get multiples of 3
        total += i
    for j in range(0, n, 5):  # Get multiples of 5
        total += j
    for k in range(0, n, 15):  # Remove double-counted multiples of 15
        total -= k
    return (total)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(submultiples(n))
