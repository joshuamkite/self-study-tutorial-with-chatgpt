import functools


cache = {0: 0, 1: 1}


def fibonacci_of(n):
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    s = 0
    i = 0
    while True:
        fib = fibonacci_of(i)
        if fib > n:
            break
        s += fib
        i += 1
    print(s)
