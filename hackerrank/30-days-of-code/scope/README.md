# Day 14: Scope

## Objective

Today we're discussing scope. Check out the Tutorial tab for learning materials and an instructional video!

The absolute difference between two integers, \(a\) and \(b\), is written as \(|a - b|\). The maximum absolute difference between two integers in a set of positive integers, \(elements\), is the largest absolute difference between any two integers in \(elements\).

The `Difference` class is started for you in the editor. It has a private integer array (`elements`) for storing non-negative integers, and a public integer (`maximumDifference`) for storing the maximum absolute difference.

## Task

Complete the `Difference` class by writing the following:

- A class constructor that takes an array of integers as a parameter and saves it to the `elements` instance variable.
- A `computeDifference` method that finds the maximum absolute difference between any two numbers in `elements` and stores it in the `maximumDifference` instance variable.

## Input Format

You are not responsible for reading any input from stdin. The locked `Solution` class in the editor reads in two lines of input. The first line contains \(N\), the size of the `elements` array. The second line has \(N\) space-separated integers that describe the `elements` array.

## Constraints

- \(1 \leq N \leq 10\)
- \(1 \leq elements[i] \leq 100\), where \(0 \leq i \leq N\).

## Output Format

You are not responsible for printing any output; the `Solution` class will print the value of the `maximumDifference` instance variable.

## Sample Input

```
3
1 2 5
```

## Sample Output

```
4
```

## Explanation

The scope of the `elements` array and `maximumDifference` integer is the entire class instance. The class constructor saves the argument passed to the constructor as the `elements` instance variable (where the `computeDifference` method can access it).

To find the maximum difference, `computeDifference` checks each element in the array and finds the maximum difference between any two elements: 

- \(|1 - 2| = 1\)
- \(|1 - 5| = 4\)
- \(|2 - 5| = 3\)

The maximum of these differences is 4, so it saves the value 4 as the `maximumDifference` variable. The locked stub code in the editor then prints the value stored as `maximumDifference` instance, which is 4.


## Input of ChatGPT

Here I had got completely confused by the request for a class constructor and was trying to do all sorts of crazy unnecessary stuff with inheritance and a new class. On putting to ChatGPT, despite asking not to, it gave the code seen here. The novel part for me is the leading double underscore so I don't feel too bad!