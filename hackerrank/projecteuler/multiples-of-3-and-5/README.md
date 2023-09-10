## [Project Euler #1: Multiples of 3 and 5](https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true)

### Problem

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below \( N \).

### Input Format

First line contains \( T \) that denotes the number of test cases. This is followed by \( T \) lines, each containing an integer, \( N \).

### Output Format

For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below \( N \).

### Constraints

$
1 \leq T \leq 10^5
$

$
1 \leq N \leq 10^9
$

### Sample Input

```plaintext
2
10
100
```
### Sample Output
```
23
2318
```

## main-too-slow.py

This was my initial attempt. I had some difficulty because I had missed the double counting which was pointed out by ChatGPT. Unfortunately I got 'time limit exceeded' when I attempted to 'submit' this code. I again referred to ChatGPT:

## main.py

> The issue with your code is that it's not optimized for large inputs. The time complexity of your function is \(O(n)\) due to the three `for` loops that iterate up to \(n\). When \(n\) is very large, this can result in a "time limit exceeded" error on platforms like HackerRank.

Unfortunately the suggested solution and variations on it di not give the right answer

## My thoughts

In order to approach this challenge correctly a mathematical approach is clearly required. At the time that I approached this problem I might have discovered the more computationally time efficient approach from traditional searching but I am not sure how well I would have been able to implement it from scratch. I was also unfamiliar with the Latex formatting for the mathematical formulae to add to the readme