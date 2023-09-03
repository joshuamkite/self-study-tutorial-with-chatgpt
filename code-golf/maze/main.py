import sys
from collections import deque


def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (0, 0)
    end = (0, 0)

    # Find start and end points
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    visited = set()
    queue = deque([(start, [])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            for px, py in path:
                if maze[px][py] != 'E':  # Keep the original 'E'
                    maze[px][py] = '.'
            return maze

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and maze[nx][ny] != '#':
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))


if __name__ == "__main__":
    # Accessing arguments
    maze_str = ""
    for arg in sys.argv[1:]:
        maze_str += arg + "\n"

    maze = [list(row) for row in maze_str.strip().split("\n")]

    solved_maze = solve_maze(maze)
    for row in solved_maze:
        print("".join(row))
