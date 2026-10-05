import matplotlib.pyplot as plt
import time

size = 70

grid = []

for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    grid.append(row)

for i in range(10, 30):
    for j in range(15, 20):
        grid[i][j] = 1

for i in range(35, 55):
    for j in range(25, 30):
        grid[i][j] = 1

for i in range(15, 20):
    for j in range(40, 60):
        grid[i][j] = 1

for i in range(45, 60):
    for j in range(45, 50):
        grid[i][j] = 1

start = (0, 0)
goal = (35, 40)

def heuristic(a, b):

    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])

    return distance


# A* algorithm
def a_star(grid, start, goal):

    open_list = []

    open_list.append(start)

    came_from = {}

    g_score = {}
    g_score[start] = 0

    f_score = {}
    f_score[start] = heuristic(start, goal)

    visited = []

    while len(open_list) > 0:

        current = open_list[0]

        for cell in open_list:

            if f_score[cell] < f_score[current]:
                current = cell

        if current == goal:

            path = []

            path.append(current)

            while current in came_from:

                current = came_from[current]

                path.append(current)

            path.reverse()

            return path, len(visited)

        open_list.remove(current)

        visited.append(current)


        moves = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for move in moves:

            new_row = current[0] + move[0]
            new_col = current[1] + move[1]

            if new_row >= 0 and new_row < size:

                if new_col >= 0 and new_col < size:

                    if grid[new_row][new_col] == 0:

                        neighbor = (new_row, new_col)


                        new_g_score = g_score[current] + 1

                        if neighbor not in g_score:

                            came_from[neighbor] = current

                            g_score[neighbor] = new_g_score

                            f_score[neighbor] = (
                                new_g_score +
                                heuristic(neighbor, goal)
                            )

                            open_list.append(neighbor)

                        else:

                            if new_g_score < g_score[neighbor]:

                                came_from[neighbor] = current

                                g_score[neighbor] = new_g_score

                                f_score[neighbor] = (
                                    new_g_score +
                                    heuristic(neighbor, goal)
                                )

    return None, len(visited)

start_time = time.time()

path, explored_count = a_star(grid, start, goal)

end_time = time.time()

computation_time = end_time - start_time

if path is None:

    print("No path found.")

else:

    print("Path found!")

    print("Path length:", len(path) - 1)

    print("Cells explored:", explored_count)

    print("Computation time:", computation_time, "seconds")


plt.figure(figsize=(8, 8))

plt.imshow(grid, cmap="Greys", origin="upper")


if path is not None:

    path_rows = []
    path_columns = []

    for cell in path:

        path_rows.append(cell[0])
        path_columns.append(cell[1])

    plt.plot(
        path_columns,
        path_rows,
        "b-",
        linewidth=2,
        label="UGV Path"
    )

plt.scatter(
    start[1],
    start[0],
    color="green",
    s=100,
    label="Start"
)

plt.scatter(
    goal[1],
    goal[0],
    color="red",
    s=100,
    label="Goal"
)

plt.title("UGV Path Planning Using A* Search")

plt.xlabel("X")

plt.ylabel("Y")

plt.legend()

plt.grid()

plt.show()