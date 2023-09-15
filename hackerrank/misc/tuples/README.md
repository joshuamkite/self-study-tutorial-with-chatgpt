# Tuples

## Task

Given an integer, `n`, and `n` space-separated integers as input, create a tuple, `t`, of those `n` integers. Then compute and print the result of `hash(t)`.

**Note:** `hash()` is one of the functions in the `__builtins__` module, so it need not be imported.

## Input Format

The first line contains an integer, `n`, denoting the number of elements in the tuple.

The second line contains `n` space-separated integers describing the elements in tuple `t`.

## Output Format

Print the result of `hash(t)`.

## Sample Input 0

```
2
1 2
```

## Sample Output 0

```
3713081631934410656
```

## Input of ChatGPT

- I was hungry and tired and initially did `arr = (input)` instead of `arr = input()`
- The hash value was incorrect.

The second point led me down quite the rabbit hole. ChatGPT suggested casting the items in my tuple to `int` but I still got a wrong answer. ChatGPT then suggested that there might be a different Python version in use- which didn't seem to make sense for an online IDE and test but then I noticed that HackerRank make 2 different Python runtimes available: `Python 3` and `Pypy 3`. This code passed with the latter but failed with the former. ChatGPT explained:

> The hash() function in Python is not guaranteed to return the same value across different runs, especially between Python 2 and Python 3 or between 32-bit and 64-bit versions of Python.
> 
> However, within a single run of a program (and typically across multiple runs in the same environment), the hash() function will return consistent values.

This was quite the eye-opener since I would expect consistent values from Linux command line hashing tools like `md5` or `sha256` 
