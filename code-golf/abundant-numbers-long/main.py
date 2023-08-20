import math


def divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:  # Avoid adding the same divisor twice
                divs.append(n // i)
    return divs


for i in range(1, 1001):
    if ((int(sum(divisors(i)))) > i):
        print(i)
