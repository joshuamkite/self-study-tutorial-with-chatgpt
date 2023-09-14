The problem "List Comprehensions" from HackerRank is described as follows:

**Problem Statement:**

You are given three integers `x`, `y`, and `z` representing the dimensions of a cuboid along with an integer `n`. You need to print a list of all possible coordinates given by `(i, j, k)` on a 3D grid where the sum of `i + j + k` is not equal to `n`. Here, `0 <= i <= x`, `0 <= j <= y`, and `0 <= k <= z`. Please use list comprehensions rather than multiple loops, as a learning exercise.

**Example:**

For `x = 1`, `y = 1`, `z = 1`, and `n = 2`, the output should be:
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

**Input Format:**
Four integers `x`, `y`, `z`, and `n`, each on a separate line.

**Output Format:**
Print the list in lexicographic increasing order.

**INput from ChatGPT**

I was stumped here so the solution is entrirely from ChatGPT (modified from below)

**Solution:**

To solve this problem using a list comprehension, you can use the following code:

```python
x, y, z, n = (int(input()) for _ in range(4))
result = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
print(result)
```

This code first takes the input values for `x`, `y`, `z`, and `n`. Then, it uses a list comprehension to generate all possible combinations of `(i, j, k)` such that their sum is not equal to `n`. The result is then printed.