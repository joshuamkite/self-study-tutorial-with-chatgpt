# Athlete Sort

## Problem

You are given a spreadsheet that contains a list of athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the \(k^{th}\) attribute and print the final resulting table. Follow the example given below for better understanding.


Note that \(k\) is indexed from 0 to \(m-1\), where \(m\) is the number of attributes.

**Note**: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

### Input Format

The first line contains \(n\) and \(m\) separated by a space. The next \(n\) lines each contain \(m\) elements. The last line contains \(k\).

### Constraints

- Each element 

### Output Format

Print the \(n\) lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

### Sample Input

```
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
```

### Sample Output

```
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
```

### Explanation

The details are sorted based on the second attribute, since \(k\) is zero-indexed.

---

**Author**: [shashank21j](https://www.hackerrank.com/profile/shashank21j)

**Difficulty**: Medium

**Max Score**: 30

**Submitted By**: [73908](https://www.hackerrank.com/challenges/python-sort-sort/leaderboard)

## Detailed explanation of lines 2 and 8 - the `map` and `lambda` functions

### Line 2: `map` function

```python
n, m = map(int, input().split())
```

1. **`input().split()`**: The `input()` function reads a line of input from the user as a string. The `split()` method then splits this string into a list of substrings based on whitespace (by default). For example, if the user enters "5 3", this will be split into `["5", "3"]`.

2. **`map(int, ...)`**: The `map()` function applies a given function to each item of an iterable (like a list) and returns a map object (an iterator). In this case, the function being applied is `int`, which converts its argument into an integer. So, `map(int, ["5", "3"])` will convert each string in the list to an integer, resulting in an iterator that yields the values `5` and `3`.

3. **`n, m = ...`**: This is a form of multiple assignment. The values produced by the iterator are unpacked into the variables `n` and `m`. So, `n` will be assigned the value `5` and `m` will be assigned the value `3`.

In summary, this line reads a space-separated string of numbers from the user, splits it, converts each number to an integer, and assigns them to `n` and `m`.

### Line 8: `lambda` function

```python
records.sort(key=lambda x: x[k])
```

1. **`lambda x: x[k]`**: This is a lambda function, which is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression. The expression is evaluated and returned when the lambda is called. In this case, the lambda takes one argument `x` (which will be an element of the `records` list) and returns the `k`-th element of `x`.

2. **`records.sort(key=...)`**: The `sort()` method sorts the list in place. The `key` argument specifies a function of one argument that is used to extract a comparison key from each element in the list. In this case, the list is sorted based on the `k`-th element of each sublist in `records`.

In summary, this line sorts the `records` list in place based on the `k`-th element of each sublist.

I hope this helps clarify the use of `map` and `lambda` in your code! If you have any more questions, feel free to ask.

## Asking if ChatGPT would improve on the passing code

Your code is already quite clean and efficient for the given problem. However, there are a few minor improvements and stylistic changes that can be made to enhance readability and maintainability:

1. **Use Descriptive Variable Names**: While `n`, `m`, and `k` are okay for short scripts or when following a problem's notation, in larger programs, it's beneficial to use more descriptive names.

2. **List Comprehension for Input**: Instead of using a for loop to populate the `records` list, you can use a list comprehension.

3. **Directly Print Using List Comprehension**: Instead of using a for loop to print each entry, you can use a list comprehension with the `print` function.

Here's a slightly revised version of your code with the above suggestions:

```python
if __name__ == '__main__':
    num_athletes, num_attributes = map(int, input().split())
    
    # Using list comprehension to read athlete records
    athlete_records = [[int(attr) for attr in input().split()] for _ in range(num_athletes)]

    sort_key_index = int(input())
    athlete_records.sort(key=lambda record: record[sort_key_index])
    
    # Directly printing using list comprehension
    [print(*record) for record in athlete_records]
```

These changes are mostly stylistic and don't impact the functionality or efficiency of your code. The choice to implement them depends on your personal coding style and the context in which the code will be used.