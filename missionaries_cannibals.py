from queue import Queue

INITIAL_STATE = (3, 3, 1)
GOAL_STATE = (0, 0, 0)
ACTIONS = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]


def is_valid(state):
    if state[0] < 0 or state[1] < 0 or state[0] > 3 or state[1] > 3:
        return False
    if state[0] > 0 and state[0] < state[1]:
        return False
    if state[0] < 3 and state[0] > state[1]:
        return False
    return True


def successors(state):
    boat = state[2]
    states = []
    for action in ACTIONS:
        if boat == 1:
            new_state = (state[0] - action[0], state[1] - action[1], 0)
        else:
            new_state = (state[0] + action[0], state[1] + action[1], 1)
        if is_valid(new_state):
            states.append(new_state)
    return states


def bfs(initial_state, goal_state):
    frontier = Queue()
    frontier.put(initial_state)
    visited = set()
    visited.add(initial_state)
    parent = {}
    while not frontier.empty():
        state = frontier.get()
        if state == goal_state:
            path = []
            while state != initial_state:
                path.append(state)
                state = parent[state]
            path.append(initial_state)
            path.reverse()
            return path
        for next_state in successors(state):
            if next_state not in visited:
                frontier.put(next_state)
                visited.add(next_state)
                parent[next_state] = state
    return None


path = bfs(INITIAL_STATE, GOAL_STATE)

if path is None:
    print("No solution found")
else:
    print("Optimal path:")
    for state in path:
        print(state)
