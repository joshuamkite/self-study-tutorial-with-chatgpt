import math


def is_fibonacci(z):
    fib_five = 5 * (z * z)
    for n in [fib_five + 4, fib_five - 4]:
        n_root_round = round(math.sqrt(n))
        n_root_resquare = n_root_round * n_root_round
        if n_root_resquare == n:
            return True
    return False


def fibonacci_property_check(z):
    if is_fibonacci(z):
        return z
    else:
        return 0


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    s = 0
    for i in range(0, n+1, 2):
        s += fibonacci_property_check(i)
    print(s)
