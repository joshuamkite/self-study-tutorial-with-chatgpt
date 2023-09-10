## Day 8: Dictionaries and Maps | HackerRank

### Objective
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-dictionaries-and-maps/tutorial) tab for learning materials and an instructional video!

### Task
Given names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each queried, print the associated entry from your phone book on a new line in the form `name=phoneNumber`; if an entry for is not found, print `Not found` instead.

**Note**: Your phone book should be a Dictionary/Map/HashMap data structure.

### Input Format
The first line contains an integer, , denoting the number of entries in the phone book. Each of the subsequent lines describes an entry in the form of space-separated values on a single line. The first value is a friend's name, and the second value is an -digit phone number. After the lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a to look up, and you must continue reading lines until there is no more input.

**Note**: Names consist of lowercase English alphabetic letters and are first names only.

### Constraints
- (Specific constraints were not provided in the scraped content)

### Output Format
On a new line for each query, print `Not found` if the name has no corresponding entry in the phone book; otherwise, print the full and in the format `name=phoneNumber`.

### Sample Input
```
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
```

### Sample Output
```
sam=99912222
Not found
harry=12299933
```

### Explanation
We add the following (Key,Value) pairs to our map so it looks like this:

We then process each query and print `key=value` if the queried is found in the map; otherwise, we print `Not found`.

Query 0: `sam` - Sam is one of the keys in our dictionary, so we print `sam=99912222`.

Query 1: `edward` - Edward is not one of the keys in our dictionary, so we print `Not found`.

Query 2: `harry` - Harry is one of the keys in our dictionary, so we print `harry=12299933`.

## Assistance from ChatGPT

I struggled working out how to get the entries greater than `n` from my remaining input. It might seem obvious but ChatGPT's suggestion based on my questoin

> What is the simplest way to get e for values greater than n for a second loop


was most helpful (but see further below)

```python

    # Second loop for values of e greater than n
    for e in range(n+1, 2*n):  # This will run the loop for values n+1 to 2n-1
     
```

I managed the rest myself with static online resources. `main-commented.py` has same code as `main.py` plus comments.

Whilst trying to understand how this code knew to pick up new lines of input I learned the below:

Me:

> ok, so why does the second loop need to reference n again, why does it not automatically start with the next line that has not already been used as the first loop does

ChatGPT:

> Great question! Let's clarify the behavior of the `input()` function and the purpose of the loop's range.
> 
> The `input()` function always reads the next available line of input. It doesn't "remember" or "know" about previous calls to `input()`. Each call to `input()` reads the next line, and then that line is "consumed", meaning it won't be read again by subsequent calls to `input()`.
> 
> Given this behavior, you're correct in observing that the second loop will automatically start reading the line immediately after the last line read by the first loop. The range of the loop (`for e in range(n+1, (n*2)+1):`) doesn't dictate which lines of input are read; it simply determines how many times the loop will iterate.
> 
> The use of `n+1` and `(n*2)+1` in the range of the second loop is actually misleading. The loop variable `e` is overwritten immediately within the loop by the line `e = input().strip()`, so the values produced by `range(n+1, (n*2)+1)` are never used for any meaningful purpose in the loop. The loop could be more clearly written as:
> 
> ```python
> for _ in range(n):
>     e = input().strip()
>     ...
> ```
> 
> Here, the underscore `_` is a common convention in Python to indicate that the loop variable is a "throwaway" variable and won't be used in the loop body. The loop still runs `n` times, which is the important part, because we expect to process `n` queries.

## follow up with ChatGPT

Although I thought I had 'solved' this code, I had not submitted it for all test cases and I later found it failing on one of them. On giving ChatGPT my code as commented and the challenge:

> Your code seems mostly correct for the given problem. You're reading the number of entries, then populating the dictionary (phone book) with the given names and phone numbers. After that, you're querying the phone book and printing the results as specified.
> 
> However, there's a minor issue. The number of queries is not necessarily equal to `n` (the number of entries in the phone book). The problem statement mentions that "there are an unknown number of lines of queries." This means you should not limit the number of queries to `n`.
> 
> To fix this, you can read queries until there's no more input. Here's a modified version of your code:
> 
> ```python
> if __name__ == '__main__':
>     book = {}
>     n = int(input().strip())
>     for _ in range(n):
>         entry = input().strip().split(" ")
>         book[entry[0]] = entry[1]
>     
>     # Read queries until there's no more input
>     while True:
>         try:
>             query = input().strip()
>             result = book.get(query, "Not found")
>             if result == "Not found":
>                 print(result)
>             else:
>                 print(f"{query}={result}")
>         except EOFError:
>             break
> ```
> 
> The `try` and `except EOFError` block will handle the case when there's no more input, and it will break out of the loop. This way, you can handle any number of queries.
> 