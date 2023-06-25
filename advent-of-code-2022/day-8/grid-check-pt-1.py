"""
read input as an array

 for each item:

set border_tree = first entry
add count border_tree to visible_trees
if next_tree is =<border_tree and < any tree to right and < any tree above in column and < any tree below in column:
    add to hidden_trees
elif next_tree is >border_tree and > any tree to right  and > any tree above in column and > any tree below in column
    add next_tree to visible_trees
add count last_tree to visible_trees
 """


import numpy as np

# Check if there is a taller or equal-height tree obstructing the view


def is_unobstructed(matrix, i, j, height):
    # Check the left direction:
    # We iterate through all elements to the left of the current position (i, j) in the same row.
    # If there is any element that is equal to or greater than the height of the current element,
    # it is obstructed from the left. If not, it is unobstructed from the left.
    unobstructed_left = not any(matrix[i, k] >= height for k in range(0, j))

    # Check the right direction:
    # Similar to the left, but we iterate to the right of the current position.
    # If there is any element equal to or greater than the height, it's obstructed from the right.
    unobstructed_right = not any(
        matrix[i, k] >= height for k in range(j+1, matrix.shape[1]))

    # Check the top direction:
    # Now, we iterate through all elements above the current position in the same column.
    # If there is any element equal to or greater than the height, it's obstructed from the top.
    unobstructed_top = not any(matrix[k, j] >= height for k in range(0, i))

    # Check the bottom direction:
    # Similar to the top, but we iterate below the current position.
    # If there is any element equal to or greater than the height, it's obstructed from the bottom.
    unobstructed_bottom = not any(
        matrix[k, j] >= height for k in range(i+1, matrix.shape[0]))

    # The tree is considered unobstructed if it is unobstructed in at least one of the directions.
    # Therefore, if it is unobstructed from the left OR right OR top OR bottom, return True.
    # Otherwise, return False.
    return unobstructed_left or unobstructed_right or unobstructed_top or unobstructed_bottom


# Check if a tree is visible


def is_visible(matrix, i, j):
    # Trees on the edge are always visible
    if i == 0 or j == 0 or i == matrix.shape[0]-1 or j == matrix.shape[1]-1:
        return True

    # Check if the tree is unobstructed by taller or equal-height trees
    return is_unobstructed(matrix, i, j, matrix[i, j])


# Read the file line by line
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Convert the lines into a list of integers
data = [[int(digit) for digit in line.strip()] for line in lines]

# Convert the list of integers into a numpy array
matrix = np.array(data)

# Variables to keep count
hidden_trees_count = 0
visible_trees_count = 0

# Iterate through each item in the matrix
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if is_visible(matrix, i, j):
            visible_trees_count += 1
        else:
            hidden_trees_count += 1

print(f"Hidden Trees Count: {hidden_trees_count}")

print(f"Visible Trees Count: {visible_trees_count}")
