network = {
    "Ali": ["Bilal", "Sara"],
    "Bilal": ["Ali", "Danish"],
    "Sara": ["Ali", "Omar"],
    "Danish": ["Bilal", "Hira"],
    "Omar": ["Sara"],
    "Hira": ["Danish"]
}

def bfs_shortest_path(graph, start, goal):
    queue = [[start]]
    visited = [start]

    while queue:
        path = queue.pop(0)
        person = path[-1]

        if person == goal:
            return path

        for friend in graph[person]:
            if friend not in visited:
                visited.append(friend)
                new_path = path + [friend]
                queue.append(new_path)

    return None

path = bfs_shortest_path(network, "Ali", "Hira")

if path:
    print(f"Shortest chain from Ali to Hira: {path}")
    print(f"Number of introductions needed: {len(path) - 1}")
else:
    print("No connection found")