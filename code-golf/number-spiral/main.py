n = 10
matrix = [[0]*n for _ in range(n)]

num = 0
for layer in range((n + 1) // 2):
    # Define boundaries for the current layer
    start, end = layer, n - layer

    # Top row
    for j in range(start, end):
        matrix[start][j] = num
        num += 1

    # Right column
    for i in range(start + 1, end):
        matrix[i][end - 1] = num
        num += 1

    # Bottom row
    for j in range(end - 2, start - 1, -1):
        matrix[end - 1][j] = num
        num += 1

    # Left column
    for i in range(end - 2, start, -1):
        matrix[i][start] = num
        num += 1

    if num > n*n - 1:
        break

# Print the matrix
for row in matrix:
    print(' '.join(f"{x:2}" for x in row))
