# Piling Up!

There is a horizontal row of cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube `b` is on top of cube `a` then `sideLength(b) <= sideLength(a)`.

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print `Yes` if it is possible to stack the cubes. Otherwise, print `No`.

**Example Result:**
- `No`: After choosing the rightmost element, `b`, choose the leftmost element, `a`. After than, the choices are `c` and `d`. These are both larger than the top block of size `b`.
- `Yes`: Choose blocks from right to left in order to successfully stack the blocks.

**Input Format**
- The first line contains a single integer `T`, the number of test cases.
- For each test case, there are 2 lines:
  - The first line of each test case contains `n`, the number of cubes.
  - The second line contains space-separated integers, denoting the sideLengths of each cube in that order.

**Constraints**
- (The constraints are not provided in the scraped content)

**Output Format**
- For each test case, output a single line containing either `Yes` or `No`.

**Sample Input**
```
2
6
4 3 2 1 3 4
3
1 3 2
```

**Sample Output**
```
Yes
No
```

**Explanation**
- In the first test case, pick in this order: left - 4, right - 4, left - 3, right - 3, left - 2, right - 1.
- In the second test case, no order gives an appropriate arrangement of vertical cubes. `2` will always come after either `1` or `3`.

## Input of ChatGPT

some syntax guidance and correction based on examples. 

When asked for a critique on the final code:

Your code is functional and solves the problem. However, there are a few improvements and optimizations that can be made:

1. **Avoid Using `pop(0)`**: Popping the first element of a list is an O(n) operation, which can be costly for large lists. Instead, you can use pointers or indices to traverse the list.

2. **Simplify Data Collection**: Instead of storing the data in a list of tuples, you can directly process each test case.

3. **Optimize the Check**: Instead of sorting the list and then checking if it's non-decreasing, you can directly check if it's possible to stack the cubes in the desired manner.

Here's a refactored version of your code:

```python
def can_stack_cubes(cubes):
    # Use two pointers, one at the beginning and one at the end
    left, right = 0, len(cubes) - 1
    # Start with a very large value (larger than any cube)
    prev_cube = float('inf')
    
    while left <= right:
        # Choose the larger of the two ends
        if cubes[left] < cubes[right]:
            current_cube = cubes[right]
            right -= 1
        else:
            current_cube = cubes[left]
            left += 1
        
        # Check if the current cube can be placed on top of the previous one
        if current_cube > prev_cube:
            return "No"
        prev_cube = current_cube
    
    return "Yes"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        _ = int(input())  # We don't actually need to use this value
        cubes = list(map(int, input().split()))
        print(can_stack_cubes(cubes))
```

This version is more efficient and concise. The main function `can_stack_cubes` directly checks if it's possible to stack the cubes without the need for sorting.