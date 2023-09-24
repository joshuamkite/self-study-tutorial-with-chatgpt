#!/bin/python3


# Swap function from https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/


def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numberOfSwaps = 0
    for i in range(n):
        for j in range(0, n-i-1):  # Last i elements are already in place
            if a[j] > a[j+1]:
                a = swapPositions(a, j, j+1)
                numberOfSwaps += 1
            else:
                continue

    print(
        f"Array is sorted in {numberOfSwaps} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}")
