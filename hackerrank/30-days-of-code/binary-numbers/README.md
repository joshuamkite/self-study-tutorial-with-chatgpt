## Day 10: Binary Numbers

### Objective

Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

### Task

Given a base-10 integer, \( n \), convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in \( n \)'s binary representation. When working with different bases, it is common to show the base as a subscript.

**Example**

The binary representation of 5 is 101. In base 10, there are 1 and 1 consecutive ones in two groups. Print the maximum, 1.

### Input Format

A single integer, \( n \).

### Constraints

- [The constraints are not provided in the given content.]

### Output Format

Print a single base-10 integer that denotes the maximum number of consecutive 1's in the binary representation of \( n \).

**Sample Input 1**

```
5
```

**Sample Output 1**

```
1
```

**Sample Input 2**

```
13
```

**Sample Output 2**

```
2
```

### Explanation

**Sample Case 1:**

The binary representation of 5 is 101, so the maximum number of consecutive 1's is 1.

**Sample Case 2:**

The binary representation of 13 is 1101, so the maximum number of consecutive 1's is 2.

## Assistance from ChatGPT

Significant assistance from ChatGPT on this occasion:

- String slicing in the `main` function - because I did not understand the binary format prefix returned
- Refactoring the 'counter' function - I had gone down the wrong track with various operators and was trying to use `enumerate`. I sh/could have thought of the two lists and `max`ing here but I didn't.