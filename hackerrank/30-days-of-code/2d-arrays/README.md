# Day 11: 2D Arrays

## Objective

Today, we are building on our knowledge of arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video.

## Context

Given a 2D Array, `A`:

```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```

We define an hourglass in `A` to be a subset of values with indices falling in this pattern in `A`'s graphical representation:

```
a b c
  d
e f g
```

There are 16 hourglasses in `A`, and an hourglass sum is the sum of an hourglass' values.

## Task

Calculate the hourglass sum for every hourglass in `A`, then print the maximum hourglass sum.

## Example

In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.

## Input Format

There are 6 lines of input, where each line contains 6 space-separated integers that describe the 2D Array `A`.

## Constraints

- (The constraints are not mentioned in the provided content.)

## Output Format

Print the maximum hourglass sum in `A`.

## Sample Input

```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
```

## Sample Output

```
19
```

## Explanation

`A` contains the following hourglasses:

```
1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
```

The hourglass with the maximum sum (19) is:

```
2 4 4
  2
1 2 4
```
## Input of ChatGPT

`main.py` - Only static resources were used to solve this

`main-chatgpt.py` - I asked "Thanks, this is my passing code for the above challenge. could it be improved?":

> Your code is functional and solves the problem. However, there are a few improvements that can be made for clarity and efficiency:
> 
> 1. **Use Descriptive Variable Names**: Instead of using generic names like `arr`, use more descriptive names that convey the purpose of the variable.
> 2. **Avoid Unnecessary Enumerate**: You're using `enumerate` but not using the index it provides. Instead, you can use a simple range-based loop.
> 3. **Simplify Loops**: The inner loop can be simplified to avoid unnecessary slicing.
> 4. **Consistent Commenting**: Use consistent commenting throughout the code to explain the logic.
> 
> Here's a refactored version of your code:
> 
> ```python
> #!/bin/python3
> 
> def calculate_hourglass_sum(matrix):
>     # Initialize the maximum sum to a small value
>     max_sum = -63  # Since the minimum value an element can have is -9, and there are 7 elements in an hourglass, the minimum possible sum is -63
> 
>     # Loop through the rows and columns of the matrix
>     for row in range(4):  # As there are 6 rows, and an hourglass spans 3 rows, we only need to go up to the 4th row
>         for col in range(4):  # Similarly, as there are 6 columns, and an hourglass spans 3 columns, we only need to go up to the 4th column
>             top = sum(matrix[row][col:col+3])
>             middle = matrix[row+1][col+1]
>             bottom = sum(matrix[row+2][col:col+3])
>             
>             hourglass_sum = top + middle + bottom
>             max_sum = max(max_sum, hourglass_sum)
> 
>     return max_sum
> 
> if __name__ == '__main__':
>     matrix = [list(map(int, input().rstrip().split())) for _ in range(6)]
>     print(calculate_hourglass_sum(matrix))
> ```
> 
> This refactored code is more readable and slightly more efficient.

I don't think the code to set `max_sum` is needed or the comments about variable names particularly valuable. The approach to use simple `for` loops is arguably more elegant but not obviously more efficient