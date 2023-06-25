import numpy as np


def count_to_obstruction(matrix, i, j):
    height = matrix[i, j]

    # Initialize counters for each direction to 0
    count_left = 0
    count_right = 0
    count_top = 0
    count_bottom = 0

    # Count in the left direction
    for k in range(j - 1, -1, -1):
        count_left += 1
        if matrix[i, k] >= height:
            break  # Stop counting if a taller or equal tree is found

    # Count in the right direction
    for k in range(j + 1, matrix.shape[1]):
        count_right += 1
        if matrix[i, k] >= height:
            break  # Stop counting if a taller or equal tree is found

    # Count in the top direction
    for k in range(i - 1, -1, -1):
        count_top += 1
        if matrix[k, j] >= height:
            break  # Stop counting if a taller or equal tree is found

    # Count in the bottom direction
    for k in range(i + 1, matrix.shape[0]):
        count_bottom += 1
        if matrix[k, j] >= height:
            break  # Stop counting if a taller or equal tree is found

    # Multiply the counts for each direction to get the scenic score.
    return (count_left * count_right * count_top * count_bottom)


# Read the file line by line
with open('input.txt', 'r') as file:
    lines = file.readlines()

data = [[int(digit) for digit in line.strip()] for line in lines]

# Convert the list of integers into a numpy array
matrix = np.array(data)

max_scenic_score = 0

# Iterate through each item in the matrix
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        # Calculate the scenic score for the current cell
        scenic_score = count_to_obstruction(matrix, i, j)
        # Update the maximum scenic score
        max_scenic_score = max(max_scenic_score, scenic_score)

# Output the result
print(f"The maximum scenic score for any tree is {max_scenic_score}")
