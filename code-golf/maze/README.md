
## Brief

The problem from the [Code Golf Maze challenge](https://code.golf/maze#python) is as follows:

### Problem Statement

For a given maze, find the shortest path from Start to End points. Output the path in the maze with dots. 

#### Example
Input:
```
###########
#S#      E#
# ### #####
#   #     #
### ##### #
#         #
###########
```

Output:
```
###########
#S#  ....E#
#.###.#####
#...#.....#
###.#####.#
#  .......#
###########
```

Here, `S` is the start point, `E` is the end point, `#` represents walls, and spaces represent open paths. The output should show the shortest path from `S` to `E` using dots (`.`).

### Python Solution

Initial solution from ChatGPT (this was one I did not really understand how to approach myself at this point):

> You can solve this problem using Breadth-First Search (BFS) algorithm. Here's a Python code snippet to solve this problem:
> 
> ```python
> from collections import deque
> 
> def solve_maze(maze):
>     rows, cols = len(maze), len(maze[0])
>     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
>     start = (0, 0)
>     end = (0, 0)
>     
>     # Find start and end points
>     for i in range(rows):
>         for j in range(cols):
>             if maze[i][j] == 'S':
>                 start = (i, j)
>             elif maze[i][j] == 'E':
>                 end = (i, j)
>     
>     visited = set()
>     queue = deque([(start, [])])
>     
>     while queue:
>         (x, y), path = queue.popleft()
>         
>         if (x, y) == end:
>             for px, py in path:
>                 maze[px][py] = '.'
>             return maze
>         
>         visited.add((x, y))
>         
>         for dx, dy in directions:
>             nx, ny = x + dx, y + dy
>             if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and maze[nx][ny] != '#':
>                 queue.append(((nx, ny), path + [(nx, ny)]))
>                 visited.add((nx, ny))
> 
> # Example usage
> maze = [
>     list("###########"),
>     list("#S#      E#"),
>     list("# ### #####"),
>     list("#   #     #"),
>     list("### ##### #"),
>     list("#         #"),
>     list("###########")
> ]
> 
> solved_maze = solve_maze(maze)
> for row in solved_maze:
>     print("".join(row))
> ```
> 
> This code should solve the maze problem by finding the shortest path from `S` to `E` and marking it with dots.

### Further direction to ChatGPT:

> please update for accessing arguments
> ```python
> for arg in sys.argv[1:]:
> ```
and 

>we still need the original E to appear in the output

## Finished code and explanation

The finished working code is in `main.py`. I asked ChatGPT to explain how it works:

> Certainly! The code uses the Breadth-First Search (BFS) algorithm to find the shortest path from the start point `S` to the end point `E` in a given maze. Here's a breakdown of how the code works:
> 
> ### Importing Required Modules
> ```python
> import sys
> from collections import deque
> ```
> - `sys` is used to read command-line arguments.
> - `deque` from `collections` is used to implement a queue efficiently.
> 
> ### Function: `solve_maze(maze)`
> This function takes a 2D list `maze` as input and returns the solved maze.
> 
> #### Variables
> - `rows, cols`: Dimensions of the maze.
> - `directions`: A list of possible moves (up, down, left, right).
> - `start, end`: Coordinates of the start and end points.
> - `visited`: A set to keep track of visited cells.
> - `queue`: A queue to keep track of cells to visit next.
> 
> #### Finding Start and End Points
> ```python
> for i in range(rows):
>     for j in range(cols):
>         if maze[i][j] == 'S':
>             start = (i, j)
>         elif maze[i][j] == 'E':
>             end = (i, j)
> ```
> We loop through the maze to find the coordinates of `S` and `E`.
> 
> #### Breadth-First Search (BFS)
> ```python
> while queue:
>     (x, y), path = queue.popleft()
>     ...
> ```
> We use a `while` loop to perform BFS. We dequeue an element from `queue` and get its coordinates `(x, y)` and the `path` taken to reach it.
> 
> #### Checking for End Point
> ```python
> if (x, y) == end:
>     for px, py in path:
>         if maze[px][py] != 'E':
>             maze[px][py] = '.'
>     return maze
> ```
> If we reach the end point, we mark the path with dots (`.`) except for the end point `E`.
> 
> #### Exploring Neighbors
> ```python
> for dx, dy in directions:
>     nx, ny = x + dx, y + dy
>     ...
> ```
> We explore the neighboring cells and add them to the `queue` if they are valid and unvisited.
> 
> ### Main Code
> ```python
> if __name__ == "__main__":
>     ...
> ```
> This part reads the maze from command-line arguments and calls the `solve_maze()` function to solve it.
> 
> I hope this explanation helps you understand how the code works! If you have any more questions, feel free to ask.
