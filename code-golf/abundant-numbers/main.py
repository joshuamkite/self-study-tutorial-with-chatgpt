# from https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number

import math


def divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:  # Avoid adding the same divisor twice
                divs.append(n // i)
    return divs


for i in range(1, 201):
    if ((int(sum(divisors(i)))) > i):
        print(i)
