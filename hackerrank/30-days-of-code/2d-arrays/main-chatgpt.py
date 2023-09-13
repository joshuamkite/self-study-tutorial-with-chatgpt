#!/bin/python3

def calculate_hourglass_sum(matrix):
    # Initialize the maximum sum to a small value
    max_sum = -63  # Since the minimum value an element can have is -9, and there are 7 elements in an hourglass, the minimum possible sum is -63

    # Loop through the rows and columns of the matrix
    # As there are 6 rows, and an hourglass spans 3 rows, we only need to go up to the 4th row
    for row in range(4):
        for col in range(4):  # Similarly, as there are 6 columns, and an hourglass spans 3 columns, we only need to go up to the 4th column
            top = sum(matrix[row][col:col+3])
            middle = matrix[row+1][col+1]
            bottom = sum(matrix[row+2][col:col+3])

            hourglass_sum = top + middle + bottom
            max_sum = max(max_sum, hourglass_sum)

    return max_sum


if __name__ == '__main__':
    matrix = [list(map(int, input().rstrip().split())) for _ in range(6)]
    print(calculate_hourglass_sum(matrix))
