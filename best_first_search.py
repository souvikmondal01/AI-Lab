graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('D', 5), ('E', 6)],
    'C': [('F', 8)],
    'D': [],
    'E': [('G', 3)],
    'F': [('H', 2)],
    'G': [('I', 4)],
    'H': [('J', 6)],
    'I': [],
    'J': []
}


def best_first_search(graph, start, goal):
    visited = set()
    queue = [(0, start)]

    while queue:
        cost, node = queue.pop(0)
        if node == goal:
            return True

        visited.add(node)
        neighbors = graph[node]
        for neighbor, neighbor_cost in neighbors:
            if neighbor not in visited:
                queue.append((neighbor_cost, neighbor))
        queue.sort()

    return False


start = 'A'
goal = 'J'
found = best_first_search(graph, start, goal)
if found:
    print("Goal reached!")
else:
    print("Goal not found.")
