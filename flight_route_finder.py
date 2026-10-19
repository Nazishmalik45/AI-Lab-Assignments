flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": []
}
def ucs_cheapest_route(graph, start, goal):
    queue = [(0, [start])]
    visited = []
    explored = 0
    while queue:
        queue.sort()
        cost, path = queue.pop(0)
        city = path[-1]
        if city in visited:
            continue
        visited.append(city)
        explored += 1
        print("Explored path:", path, "Cost:", cost)
        if city == goal:
            return path, cost, explored
        for next_city, price in graph[city]:
            if next_city not in visited:
                new_path = path + [next_city]
                queue.append((cost + price, new_path))
    return None, 0, explored
route, cost, explored = ucs_cheapest_route(
    flights, "Islamabad", "Quetta"
)
if route:
    print("Cheapest route:", route)
    print("Total ticket cost:", cost)
    print("Total routes explored:", explored)
else:
    print("No route found")

print("Total routes explored:", explored)