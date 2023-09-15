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

not used for initial solution but invited to critique it 

**N.B.** See note following critique

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

**N.B.** This code as an initially suggested has an error in `students.append`. The corrected, validated version is in `main-chatgpt.py`

Whilst the `append` improvement was clear to me I asked for more detail about the later functions improvements:

> this works now but please explain the change from 
>
> ```python
>     college2 = [[item[0],item[1]] for item in students if item[1] !=(students[0][1])] # reconstruct list if lowest score not present, i.e. remove lowest score
> ```
> to
> 
> ```python
> # Find the second lowest score
>     second_lowest_score = next(student[1] for student in students if student[1] != students[0][1])
> ```

> Certainly! Let's break down the change:
> 
> ### Original Code:
> 
> ```python
> college2 = [[item[0], item[1]] for item in students if item[1] != (students[0][1])]
> ```
> 
> This line creates a new list `college2` that contains all students except those with the lowest score. It does this by iterating over each student in the `students` list and checking if their score is not equal to the score of the first student (which, after sorting, is the lowest score). If the condition is met, the student is added to the `college2` list.
> 
> ### New Code:
> 
> ```python
> second_lowest_score = next(student[1] for student in students if student[1] != students[0][1])
> ```
> 
> This line finds the second lowest score directly without creating an intermediate list like `college2`. Here's how it works:
> 
> 1. **Generator Expression**: 
>     - `(student[1] for student in students if student[1] != students[0][1])` is a generator expression. It's similar to a list comprehension but doesn't generate a list in memory. Instead, it yields items one by one.
>     - This generator yields scores of all students whose score is not the lowest (i.e., not equal to `students[0][1]`).
> 
> 2. **`next()` Function**:
>     - The `next()` function retrieves the next item from an iterator (in this case, our generator expression).
>     - Since the `students` list is sorted, the first score yielded by our generator will be the second lowest score, because we've excluded the lowest score with our condition.
> 
> By using this approach, we directly get the second lowest score without the need to create an intermediate list. This makes the code more efficient, especially when dealing with large lists, and also simplifies the logic by removing the need for the `college2` list.

> please also explain change from
> 
> ```python
>     college3 = [item[0] for item in college2 if item[1] == (college2[0][1]) ] # reconstruct list of only names if score == lowest in college2
> ```
> to
> ```python
> # Filter names with the second lowest score and sort them
>     second_lowest_names = sorted([student[0] for student in students if student[1] == second_lowest_score])
> ```

> Of course! Let's break down the changes:
> 
> ### Original Code:
> 
> ```python
> college3 = [item[0] for item in college2 if item[1] == (college2[0][1])]
> ```
> 
> In this line:
> - You're creating a new list `college3` that contains the names of students who have the second lowest score.
> - You determine the second lowest score by looking at the first student in the `college2` list (which has already excluded students with the lowest score). Therefore, the score of the first student in `college2` is the second lowest score.
> - You then iterate over each student in `college2` and check if their score matches this second lowest score. If it does, you add their name to the `college3` list.
> 
> ### New Code:
> 
> ```python
> second_lowest_names = sorted([student[0] for student in students if student[1] == second_lowest_score])
> ```
> 
> In this line:
> - Instead of using an intermediate list like `college2`, we directly filter the names from the original `students` list based on the `second_lowest_score` we found earlier.
> - We use a list comprehension to iterate over each student in the `students` list and check if their score matches the `second_lowest_score`. If it does, we add their name to the resulting list.
> - We then sort the resulting list of names using the `sorted()` function to ensure they are in alphabetical order.
> 
> ### Explanation:
> 
> The main difference between the two approaches is the elimination of the intermediate list (`college2`) and the direct use of the `second_lowest_score` variable to filter names from the original `students` list.
> 
> The new approach is more efficient and concise:
> 1. **Efficiency**: By eliminating the need for the intermediate `college2` list, we reduce the number of iterations and memory usage.
> 2. **Conciseness**: The new code is more straightforward because it directly expresses the intent: "Get the names of students with the second lowest score and sort them." There's no need to first exclude students with the lowest score and then determine the second lowest score from the resulting list.
> 
> By directly working with the `students` list and the `second_lowest_score` variable, the logic becomes clearer and easier to follow.