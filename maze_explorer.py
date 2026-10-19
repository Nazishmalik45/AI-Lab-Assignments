maze = {
    "Entrance": ["Hall1", "Hall2"],
    "Hall1": ["Room1"],
    "Hall2": ["Room2", "Trap"],
    "Room1": [],
    "Room2": ["Exit"],
    "Trap": [],
    "Exit": []
}
def dfs_can_reach(maze, start, exit_room):
    stack = [start]
    visited = []
    while stack:
        room = stack.pop()
        if room not in visited:
            visited.append(room)
            if room == exit_room:
                print("Visit order:", visited)
                return True
            for next_room in reversed(maze[room]):
                if next_room not in visited:
                    stack.append(next_room)
    print("Visit order:", visited)
    return False
result = dfs_can_reach(maze, "Entrance", "Exit")
print(f"Can reach Exit from Entrance? {result}")