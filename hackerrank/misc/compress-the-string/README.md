# Compress the String!

In this task, we would like for you to appreciate the usefulness of the `groupby()` function of `itertools`. To read more about this function, [Check this out](https://docs.python.org/2/library/itertools.html#itertools.groupby).

You are given a string `S`. Suppose a character `'c'` occurs consecutively `X` times in the string. Replace these consecutive occurrences of the character `'c'` with `(X, c)` in the string.

For a better understanding of the problem, check the explanation.

## Input Format

A single line of input consisting of the string `S`.

## Output Format

A single line of output consisting of the modified string.

## Constraints

- All the characters of `S` denote integers between `0` and `9`.

## Sample Input

```
1222311
```

## Sample Output

```
(1, 1) (3, 2) (1, 3) (2, 1)
```

## Explanation

First, the character `1` occurs only once. It is replaced by `(1, 1)`. Then the character `2` occurs three times, and it is replaced by `(3, 2)` and so on. Also, note the single space within each compression and between the compressions.

## INput from ChatGPT

I arrived at the code in `main.py` using only static resources but I felt that constructing tuples in this way was a bit of a hack and so asked ChatGPT if this could be improved:

> Your code is already quite concise and makes good use of the `groupby` function from the `itertools` module. However, there are a few minor improvements and stylistic changes you can make:
> 
> 1. You don't need to convert the input string to a list. Strings are already iterable, so you can directly use the `groupby` function on the input string.
> 
> 2. Instead of printing each tuple one by one, you can construct a list of tuples and then print them all at once. This can make the code slightly more readable.
> 
> Here's a slightly refactored version of your code:
> 
> ```python
> from itertools import groupby
> 
> if __name__ == "__main__":
>     s = input()
>     
>     compressed = [(len(list(group)), int(key)) for key, group in groupby(s)]
>     
>     print(*compressed)
> ```
> 
> Note: The `print(*compressed)` statement uses argument unpacking to print each tuple in the `compressed` list separated by a space. This achieves the same result as your `end=' '` parameter in the original print statement.