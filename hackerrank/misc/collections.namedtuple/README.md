# Collections.namedtuple()

**Basically, namedtuples are easy to create, lightweight object types.** They turn tuples into convenient containers for simple tasks. With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

**Example Code 01:**

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11
```

**Code 02:**

```python
>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y
```

## Task

Dr. John Wesley has a spreadsheet containing a list of student's `ID`, `MARKS`, `CLASS`, and `NAME`. Your task is to help Dr. Wesley calculate the average marks of the students.

**Note:**

1. Columns can be in any order. IDs, marks, class, and name can be written in any order in the spreadsheet.
2. Column names are `ID`, `MARKS`, `CLASS`, and `NAME`. (The spelling and case type of these names won't change.)

**Input Format:**

The first line contains an integer `N`, the total number of students. The second line contains the names of the columns in any order. The next `N` lines contains the `ID`, `MARKS`, `CLASS`, and `NAME`, under their respective column names.

**Constraints:**

[Constraints are not provided in the scraped content.]

**Output Format:**

Print the average marks of the list corrected to 2 decimal places.

**Sample Input TESTCASE 01:**

```
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
```

**TESTCASE 02:**

```
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
```

**Sample Output TESTCASE 01:**

```
78.00
```

**TESTCASE 02:**

```
81.00
```

**Explanation TESTCASE 01:**

Average = [Explanation not provided in the scraped content.]

**Note:** Can you solve this challenge in `4 lines of code or less`? There is `no penalty` for solutions that are correct but have more than 4 lines.

## My experience

I was in a hurry after a long day, and whilst I could appreciate what a named tuple is, I was struggling somewhat conceptually with getting the name for the tuple from an unordered list. Since named tuples seemed like a somewhat 'extra' feature I elected to solve the challenge with zipmap instead - `main-zipmap.py` On asking ChatGPT about a named tuple approach it offered `main-namedtuple.py` witht eh following explanation:

> Using `namedtuple` from the `collections` module can make your code more readable and structured. Named tuples are essentially a way to create simple classes for storing data without the overhead of defining a full class. They can be more memory efficient than dictionaries and can be used to make the code more self-documenting.
> 
> Benefits of using `namedtuple`:
> 
> 1. **Readability**: Accessing attributes by name (like `student.MARKS`) can be more readable than dictionary keys.
> 2. **Memory Efficiency**: Named tuples can be more memory efficient than dictionaries.
> 3. **Immutable**: Named tuples are immutable, which can prevent accidental modification of data.
> 
> However, whether or not to use `namedtuple` depends on the specific use case and personal preference. If you find that using dictionaries is more intuitive or if the structure of the data might change frequently, sticking with dictionaries might be a better choice. On the other hand, if you want a more structured and memory-efficient approach, `namedtuple` is a great option.

Imports and comments aside, it seems that there are 3 x meaningful differences from the zipmap function:

Additional lines for named tuples version:

`from collections import namedtuple`
`Student = namedtuple('Student', headers)`

I had previously figured out these 2 for myself!

Changed lines for named tuples version:

`student = dict(zip(headers, rec))` => `student = Student(*rec)`
`score.append(int(student['MARKS']))` => `scores.append(int(student.MARKS))`

I can't comment on memory efficiency. Immutability could be a clear benefit but I am sceptical that these changes improve readability. On reflection, I did not need to worry about the name of my named tuple- just like with the zipmap function, a separate top-level name for each instance of the collection was not needed.

