def sum_of_multiples(x, n):
    m = (n - 1) // x
    return x * m * (m + 1) // 2


def submultiples(n):
    return sum_of_multiples(3, n) + sum_of_multiples(5, n) - sum_of_multiples(15, n)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(submultiples(n))
