
# 8-Puzzle Problem using BFS

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Function to print the puzzle
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Generate all possible moves
def get_neighbours(state):
    neighbours = []

    zero = state.index(0)  # Position of blank
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = (
                new_state[new_zero], new_state[zero]
            )

            neighbours.append(tuple(new_state))

    return neighbours

# BFS algorithm
def bfs(start):
    queue = [(start, [start])]
    visited = set()

    while queue:
        state, path = queue.pop(0)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path

        for neighbour in get_neighbours(state):
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    return None

# Example start state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

# Find solution
solution = bfs(start)

if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")

    for step in solution:
        print_board(step)
else:
    print("No solution found")
