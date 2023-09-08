## Day 7: Arrays

### Objective
Today, we will learn about the Array data structure. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-arrays/tutorial) tab for learning materials and an instructional video.

### Task
Given an array, `A`, of integers, print `A`'s elements in reverse order as a single line of space-separated numbers.

**Example:**  
Input: `1 2 3 4`  
Output: `4 3 2 1`

Each integer is separated by one space.

### Input Format
The first line contains an integer, `n` (the size of our array).  
The second line contains space-separated integers that describe array `A`'s elements.

### Constraints
- `n` is the size of the array.
- `A[i]` is an integer in the array.

### Output Format
Print the elements of array `A` in reverse order as a single line of space-separated numbers.

### Sample Input
```
4
1 4 3 2
```

### Sample Output
```
2 3 4 1
```

## Assistance from ChatGPT

I was a bit thrown at the map rather than a list and how to reverse it. ChatGPT suggested this to print my reversed array without parentheses

```python
print(' '.join(map(str, arr)))
```