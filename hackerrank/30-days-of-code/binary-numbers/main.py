#!/bin/python3


def counter(n):
    max_count = 0
    current_count = 0
    for v in n:
        if v == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count


if __name__ == '__main__':
    n = int(input().strip())
    b = [*(bin(n)[2:])]  # Slice the string to remove the '0b' prefix
    print(counter(b))
