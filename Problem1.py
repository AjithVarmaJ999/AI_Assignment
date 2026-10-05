
import pandas as pd

data = pd.read_csv("indian-cities-dataset.csv")

graph = {}

for i in range(len(data)):
    city1 = data["Starting"][i]
    city2 = data["Destination"][i]
    distance = data["Distance"][i]

    if city1 not in graph:
        graph[city1] = []

    if city2 not in graph:
        graph[city2] = []

    # Bidirectional
    graph[city1].append([city2, distance])
    graph[city2].append([city1, distance])

def dijkstra(graph, start, goal):

    # Initially, all distances are infinity
    distances = {}

    for city in graph:
        distances[city] = float("inf")

    distances[start] = 0

    previous = {}

    for city in graph:
        previous[city] = None

    unvisited = []

    for city in graph:
        unvisited.append(city)

    while len(unvisited) > 0:

        current = None
        shortest_distance = float("inf")

        for city in unvisited:
            if distances[city] < shortest_distance:
                shortest_distance = distances[city]
                current = city

        if current is None:
            break

        if current == goal:
            break

        unvisited.remove(current)

        for neighbor, road_distance in graph[current]:

            new_distance = distances[current] + road_distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current

    if distances[goal] == float("inf"):
        return None, float("inf")

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path, distances[goal]

print("Available cities:")

for city in graph:
    print(city)

# Source and Destination
start = input("\nEnter starting city: ").strip()
goal = input("Enter destination city: ").strip()


if start not in graph or goal not in graph:
    print("City not found in the dataset.")

else:
    path, total_distance = dijkstra(graph, start, goal)

    if path is None:
        print("No route exists between these cities.")

    else:
        print("\nShortest path:")

        for i in range(len(path)):
            print(path[i], end="")

            if i < len(path) - 1:
                print(" -> ", end="")

        print()

        print("\nRoad distances:")

        for i in range(len(path) - 1):
            city1 = path[i]
            city2 = path[i + 1]

            for neighbor, distance in graph[city1]:
                if neighbor == city2:
                    print(city1, "to", city2, "=", distance, "km")
                    break

        print("\nTotal shortest distance:",
              total_distance, "km")