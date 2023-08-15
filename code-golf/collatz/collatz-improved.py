def stopping_time(n):
    i = 0
    while n != 1:
        if n % 2 == 0:  # If n is even
            n = n / 2  # divide it by 2
        else:  # otherwise
            n = (n * 3) + 1  # multiply by 3 and then add 1.
        i += 1  # increment the step count
    return i


for n in range(1, 1001):
    print(stopping_time(n))
