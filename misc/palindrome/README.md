https://pythonprinciples.com/challenges/Palindrome/

Challenge
Palindrome
A string is a palindrome when it is the same when read backwards.

For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".

Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.

## Solution

I needed to use ChatGPT to help with syntax (and I had tried to use type hinting (incorrectly)):

what's wrong with this

```python
def palindrome(b, string):
    a = [*b]
    c = a.reverse()
    if a == c:
        return True
    else:
        return False
```

The code you provided has a few issues:

1. The function `palindrome` takes two arguments `b` and `string`, but only uses `b`. The `string` argument is not used in the function.

2. The `reverse()` method of a list modifies the list in-place and returns `None`. So, when you do `c = a.reverse()`, `c` will be assigned the value `None`.

3. The comparison `if a == c:` will always evaluate to `False` because `c` is `None`.

Here's a corrected version of the function:

```python
def palindrome(b):
    a = list(b)
    c = a.copy()
    a.reverse()
    if a == c:
        return True
    else:
        return False
```

Or, more concisely:

```python
def palindrome(b):
    return list(b) == list(b)[::-1]
```

Note that I've removed the `string` argument since it wasn't being used. If you intended to use it, please provide more context on its purpose.