# Nested Lists

Given the names and grades for each student in a class of students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

**Note:** If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

**Example:**

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

```
alpha
beta
```

**Input Format:**

- The first line contains an integer, , the number of students.
- The subsequent lines describe each student over lines.
  - The first line contains a student's name.
  - The second line contains their grade.

**Constraints:**

There will always be one or more students having the second lowest grade.

**Output Format:**

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

**Sample Input 0:**

```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

**Sample Output 0:**

```
Berry
Harry
```

**Explanation 0:**

There are students in this class whose names and grades are assembled to build the following list:

```python
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
```

The lowest grade of belongs to Tina. The second lowest grade of belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

## ChatGPT

not used for initial solution but invited to critique it:

> Your code is functional and solves the problem. However, there are several areas where it can be improved for readability, efficiency, and simplicity:
> 
> 1. **Use Descriptive Variable Names**: Instead of `college`, `college2`, and `college3`, use more descriptive names to make the code more readable.
> 
> 2. **Directly Append to List**: Instead of creating a temporary `student` list and then appending it to `college`, you can directly append the name and score as a list to `college`.
> 
> 3. **Simplify Sorting and Filtering**: The process of sorting and filtering can be simplified using list comprehensions.
> 
> Here's a refactored version of your code:
> 
> ```python
> if __name__ == '__main__':
>     students = []
>     for _ in range(int(input())):
>         name = input()
>         score = float(input())
>         students.append([name, score])
> 
>     # Sort by score
>     students.sort(key=lambda x: x[1])
> 
>     # Find the second lowest score
>     second_lowest_score = next(student[1] for student in students if student[1] != students[0][1])
> 
>     # Filter names with the second lowest score and sort them
>     second_lowest_names = sorted([student[0] for student in students if student[1] == second_lowest_score])
> 
>     # Print the names
>     for name in second_lowest_names:
>         print(name)
> ```
> 
> Changes made:
> 
> - Used the name `students` instead of `college` for clarity.
> - Removed the intermediate lists `college2` and `college3`.
> - Used a generator expression with `next()` to find the second lowest score.
> - Used a list comprehension to filter and sort names with the second lowest score.