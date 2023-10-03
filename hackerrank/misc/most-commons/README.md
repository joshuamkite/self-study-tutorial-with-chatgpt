## Problem

A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. 

Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string. 

Print the three most common characters along with their occurrence count. Sort in descending order of occurrence count. If the occurrence count is the same, sort the characters in alphabetical order. 

For example, according to the conditions described above, would have its logo with the letters .

### Input Format

A single line of input containing the string .

### Constraints

- has at least 3 distinct characters

### Output Format

Print the three most common characters along with their occurrence count each on a separate line. Sort output in descending order of occurrence count. If the occurrence count is the same, sort the characters in alphabetical order.

### Sample Input 0

```
aabbbccde
```

### Sample Output 0

```
b 3
a 2
c 2
```

### Explanation 0

Here, `b` occurs 3 times. It is printed first. Both `a` and `c` occur 2 times. So, `a` is printed in the second line and `c` in the third line because `a` comes before `c` in the alphabet.

**Note**: The string has at least 3 distinct characters.

## Input of ChatGPT

- Here I was able to create the initial score_map on my own but I had some errors with the syntax for checking if a key already existed.
- I then had an initial lambda function based on research on StackOverflow but was struggling to adapt it to my purpose.

Here I arrived at 

```python
sorted_list = sorted(score_map.items(), key=lambda item: (-item[1], item[0]))
```
based on dialogue with ChatGPT which provided this explanation (note: score_map was my own creation):

1. **`score_map.items()`**:
    - `score_map` is a dictionary where keys are characters and values are their frequencies (or scores).
    - The `items()` method returns an iterable of the dictionary's key-value pairs as tuples. For example, if `score_map = {'a': 3, 'b': 1}`, then `score_map.items()` would produce `[('a', 3), ('b', 1)]`.

2. **`lambda item: (-item[1], item[0])`**:
    - This is a lambda function, which is a small anonymous function in Python.
    - The lambda function takes an argument `item`, which is a tuple from `score_map.items()`.
    - It returns a tuple where:
        - The first element is `-item[1]`, which is the negative value of the frequency. This is used to sort the characters in descending order based on their frequencies.
        - The second element is `item[0]`, which is the character itself. This is used to sort characters alphabetically if their frequencies are the same.

3. **`sorted(..., key=lambda item: (-item[1], item[0]))`**:
    - The `sorted()` function sorts an iterable based on the specified key.
    - The `key` argument specifies a function that extracts a comparison key from each element of the iterable. In this case, the lambda function is used to extract a tuple key for sorting.
    - The sorting happens in two stages:
        1. First, it sorts based on the frequencies in descending order (because of the negative sign in `-item[1]`).
        2. If two characters have the same frequency, it then sorts them alphabetically in ascending order (because of `item[0]`).

In summary, this line of code sorts the key-value pairs of the `score_map` dictionary based on their values (frequencies) in descending order. If two characters have the same frequency, they are sorted alphabetically. The result is a list of tuples, which is stored in the `sorted_list` variable.