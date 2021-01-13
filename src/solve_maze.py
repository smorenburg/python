maze = [
    ['.', '.', '.', '.'],
    ['.', 'x', 'x', 'x'],
    ['.', '.', '.', 'x'],
    ['x', 'x', '.', '.']
]

maze2 = [
    ['.', '.', '.', '.'],
    ['x', 'x', 'x', 'x'],
    ['.', '.', '.', 'x'],
    ['x', 'x', '.', '.']
]

maze3 = [
    ['.', '.', '.', '.'],
    ['x', 'x', 'x', 'x'],
    ['.', '.', '.', 'x'],
    ['x', 'x', '.', '.']
]


def print_maze(maze):
    for row in maze:
        row_prt = ''
        for value in row:
            row_prt += f'{value} '
        print(row_prt)


def solve_maze(maze):
    """
    >>> solve_maze(maze)
    ['d', 'd', 'r', 'r', 'd', 'r']
    >>> solve_maze_helper(maze2, [], 0, 0)
    """
    if len(maze) < 1:
        return None

    if len(maze[0]) < 1:
        return None

    return solve_maze_helper(maze, [], 0, 0)


def solve_maze_helper(maze, sol, pos_row, pos_col):
    """
    >>> solve_maze_helper(maze, [], 0, 0)
    ['d', 'd', 'r', 'r', 'd', 'r']
    >>> solve_maze_helper(maze2, [], 0, 0)
    >>> solve_maze_helper(maze3, [], 0, 0)
    ['r', 'r', 'r', 'd', 'd', 'd']
    """
    # Get the size of the maze
    num_row = len(maze)
    num_col = len(maze[0])

    # Base cases

    # Robot is already home
    if pos_row == num_row - 1 and pos_col == num_col - 1:
        return sol

    # Out of bounds
    if pos_row >= num_row or pos_col >= num_col:
        return None

    # Is on an obstacle
    if maze[pos_row][pos_col] == 'x':
        return None

    # Try going right
    sol.append('r')
    sol_going_right = solve_maze_helper(maze, sol, pos_row, pos_col + 1)
    if sol_going_right is not None:
        return sol_going_right

    # Going right doesn't work, backtrack, try going down
    sol.pop()
    sol.append('d')
    sol_going_down = solve_maze_helper(maze, sol, pos_row + 1, pos_col)
    if sol_going_down is not None:
        return sol_going_down

    # No solution, impossible, backtrack
    sol.pop()
    return None
