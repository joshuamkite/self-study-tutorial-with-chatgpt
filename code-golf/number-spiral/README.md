https://code.golf/number-spiral#python

## Brief

Print a 10×10 grid of the numbers 0 to 99 inclusive. Starting at the top left the numbers should spiral clockwise towards the centre, be right aligned, and have a space between each number.

The full grid should look like this:
```
 0  1  2  3  4  5  6  7  8  9
35 36 37 38 39 40 41 42 43 10
34 63 64 65 66 67 68 69 44 11
33 62 83 84 85 86 87 70 45 12
32 61 82 95 96 97 88 71 46 13
31 60 81 94 99 98 89 72 47 14
30 59 80 93 92 91 90 73 48 15
29 58 79 78 77 76 75 74 49 16
28 57 56 55 54 53 52 51 50 17
27 26 25 24 23 22 21 20 19 18
```

## main.py

Although I had some idea of how I wanted to approach this, I really struggled to describe this coherently. Whilst I thought it would be more efficient to compose the series as a 2-dimensional array, I thought it might be easier to decompose it as diminishing lists in a pattern. I found myself getting bogged down however and could not easily find a relevant tutorial appropriate to my level. I put it to ChatGPT but I had to have extended dialogue to ensure the correct start and end values. 

> i don't think this is the issue. this code starts at 1 when it should start at 0 and ends at 100 when it should end at 99

The resulting application is purely ChatGPT with my direction:

## Conversation with ChatGPT 

I asked ChatGPT to make code simpler and clearer and to explain how this works:

> Of course! Let's break down the code step by step:
> 
> 1. **Initialization**:
> ```python
> n = 10
> matrix = [[0]*n for _ in range(n)]
> num = 0
> ```
> Here, we're setting up a square matrix of size `n x n` filled with zeros. The variable `num` will be used to fill the matrix and starts at 0.
> 
> 2. **Loop through Layers**:
> ```python
> for layer in range((n + 1) // 2):
> ```
> The matrix is filled layer by layer, starting from the outermost layer and moving inwards. For a matrix of size `n x n`, there will be `(n + 1) // 2` layers. For example, a `4x4` matrix has 2 layers, and a `5x5` matrix also has 3 layers.
> 
> 3. **Define Boundaries**:
> ```python
> start, end = layer, n - layer
> ```
> For each layer, we define a `start` and an `end` boundary. These boundaries help us determine where to start and stop filling numbers for the current layer.
> 
> 4. **Filling the Matrix**:
> - **Top Row**:
>   ```python
>   for j in range(start, end):
>       matrix[start][j] = num
>       num += 1
>   ```
>   We fill the top row of the current layer from left to right.
> 
> - **Right Column**:
>   ```python
>   for i in range(start + 1, end):
>       matrix[i][end - 1] = num
>       num += 1
>   ```
>   Next, we fill the rightmost column of the current layer from top to bottom.
> 
> - **Bottom Row**:
>   ```python
>   for j in range(end - 2, start - 1, -1):
>       matrix[end - 1][j] = num
>       num += 1
>   ```
>   We then fill the bottom row of the current layer from right to left.
> 
> - **Left Column**:
>   ```python
>   for i in range(end - 2, start, -1):
>       matrix[i][start] = num
>       num += 1
>   ```
>   Finally, we fill the leftmost column of the current layer from bottom to top.
> 
> 5. **Exit Condition**:
> ```python
> if num > n*n - 1:
>     break
> ```
> Once the number `num` exceeds `n*n - 1` (which is 99 for a `10x10` matrix), we break out of the loop. This ensures that we don't overfill the matrix.
> 
> 6. **Printing the Matrix**:
> ```python
> for row in matrix:
>     print(' '.join(f"{x:2}" for x in row))
> ```
> Lastly, we print the matrix row by row. The `f"{x:2}"` format string ensures that each number occupies at least two spaces, so the matrix is printed neatly.
> 
> In essence, the code fills the matrix in a spiral pattern, layer by layer, starting from the outermost layer and moving inwards.
> 

I asked: 

> thanks but I don't understand what is controlling the direction in which we fill the matrix:
 
> Certainly! The direction in which the matrix is filled is controlled by the sequence of loops and the range of indices used in each loop. Let's break down the directional control:
> 
> 1. **Top Row (Left to Right)**:
> ```python
> for j in range(start, end):
>     matrix[start][j] = num
>     num += 1
> ```
> Here, the row index `i` is fixed at `start`, and the column index `j` varies from `start` to `end-1`. This fills the top row of the current layer from left to right.
> 
> 2. **Right Column (Top to Bottom)**:
> ```python
> for i in range(start + 1, end):
>     matrix[i][end - 1] = num
>     num += 1
> ```
> The column index `j` is fixed at `end-1`, and the row index `i` varies from `start+1` to `end-1`. This fills the rightmost column of the current layer from top to bottom.
> 
> 3. **Bottom Row (Right to Left)**:
> ```python
> for j in range(end - 2, start - 1, -1):
>     matrix[end - 1][j] = num
>     num += 1
> ```
> The row index `i` is fixed at `end-1`, and the column index `j` decreases from `end-2` to `start`. This fills the bottom row of the current layer from right to left.
> 
> 4. **Left Column (Bottom to Top)**:
> ```python
> for i in range(end - 2, start, -1):
>     matrix[i][start] = num
>     num += 1
> ```
> The column index `j` is fixed at `start`, and the row index `i` decreases from `end-2` to `start+1`. This fills the leftmost column of the current layer from bottom to top.
> 
> The sequence of these loops (top row -> right column -> bottom row -> left column) and the range of indices used in each loop dictate the spiral direction in which the matrix is filled. The outer `for` loop ensures that this sequence is repeated for each layer, starting from the outermost layer and moving inwards.