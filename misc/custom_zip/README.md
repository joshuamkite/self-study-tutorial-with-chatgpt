# Challenge

## Custom zip

The built-in zip function "zips" two lists. Write your own implementation of this function.

Define a function named zap. The function takes two parameters, a and b. These are lists.

Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.

You may assume a and b have equal lengths.

If you don't get it, think of a zipper.

For example:

```python
zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
)
```
Should return:
```python
[(0, 5),
 (1, 6),
 (2, 7),
 (3, 8)]
```

## ChatGPT input

I was attempting

```python
def zap(a, b):
    zop=[]
    for i in a:
        zop.append(tuple([(a[i]),(b[i])]))
    return zop    
```

ChatGPT advised:

> The function you provided is attempting to pair elements from two lists `a` and `b` into tuples and then append those tuples to the `zop` list. However, there's an issue with the way you're trying to access the elements of `a` and `b`.
> 
> Here's the problematic line:
> ```python
> zop.append(tuple([(a[i]),(b[i])]))
> ```
> 
> In the context of the loop, `i` is an element of `a`, not an index. So, when you use `a[i]`, you're trying to use the element of `a` as an index, which will raise an error if the element is not a valid index or if it's out of range.
> 
> To fix this, you can use the `enumerate` function to loop through the indices and elements of `a`:
> 
> ```python
> def zap(a, b):
>     zop = []
>     for i, val in enumerate(a):
>         zop.append((val, b[i]))
>     return zop
> ```
> 
> This will correctly pair the elements of `a` and `b` into tuples. However, make sure that `a` and `b` have the same length, otherwise you'll get an `IndexError` when trying to access an element in `b` that doesn't exist. If the lists can have different lengths and you want to handle that gracefully, you might consider using Python's built-in `zip` function.

I had not come across `enumerate` before, unfortunately, despite it clearly being a somewhat fundamental function in Python. [This article](https://realpython.com/python-enumerate/) sums up my journey and the issues surprisingly accurately. I had thought I would need to create a map and was looking fo[answers on StackOverflow like this](https://stackoverflow.com/questions/40912089/python-map-on-zipped-object). This is the sort of occasion where an interactive tutor is of special value- falling into an 'X and Y problem situation'