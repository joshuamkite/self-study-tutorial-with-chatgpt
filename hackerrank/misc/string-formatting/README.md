# String Formatting

Given an integer, `n`, print the following values for each integer from `1` to `n`:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

### Function Description

Complete the `print_formatted` function in the editor below.

`print_formatted` has the following parameters:
- `int number`: the maximum value to print

### Prints

The four values must be printed on a single line in the order specified above for each `i` from `1` to `n`. Each value should be space-padded to match the width of the binary value of `n` and the values should be separated by a single space.

### Input Format

A single integer denoting `n`.

### Constraints

- \(1 \leq n \leq 99\)

### Sample Input

```
17
```

### Sample Output

```
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
```

## input of ChatGPT

I had misunderstood the syntax for `ljustify` and was trying to do an unnecessary calculation. I had also not correctly scoped my width evaluation. The corrected (and simplified!)working version is in `main.py` as can be seen from ChatGPT's `main-improved.py` my original pattern was excessively complex and it is better to simply `rjustify` everything without any complex evaluations and list rebuilding.