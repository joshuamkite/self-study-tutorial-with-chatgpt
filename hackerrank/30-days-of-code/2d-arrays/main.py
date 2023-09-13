#!/bin/python3

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hourglass = []  # empty list for appending to

    for row, _ in enumerate(arr[0:4][0:4]):    # slice array to get first 3 rows

        # slice array to get first 3 columns
        for col, _ in enumerate(arr[0][0:4]):

            hourglass.append(
                (
                    # top 3 elements of hourglass
                    arr[row][col]+arr[row][col+1]+arr[row][col+2]
                    + arr[row+1][col+1]  # waist of hourglass
                    + arr[row+2][col]+arr[row+2][col+1] + \
                    arr[row+2][col+2]  # bottom 3 elements of hourlgass
                )
            )
    print(max(hourglass))  # print max value from list
