#Depth Limited Search

from queue import Queue

def bidirectional_search(start_state, goal_state, successors):
    
    forward_visited = set()
    backward_visited = set()

    
    forward_queue = Queue()
    backward_queue = Queue()

  
    forward_queue.put(start_state)
    backward_queue.put(goal_state)


    forward_visited.add(start_state)
    backward_visited.add(goal_state)

    while not forward_queue.empty() and not backward_queue.empty():
       
        curr_state = forward_queue.get()
        for successor in successors(curr_state):
            if successor not in forward_visited:
                forward_visited.add(successor)
                forward_queue.put(successor)
            if successor in backward_visited:
                return (curr_state, successor)

        curr_state = backward_queue.get()
        for successor in successors(curr_state):
            if successor not in backward_visited:
                backward_visited.add(successor)
                backward_queue.put(successor)
            if successor in forward_visited:
                return (successor, curr_state)

    return None



start_state = ((1, 2, 3), (4, 5, 6), (7, 8, None))
goal_state = ((1, 2, 3), (4, 5, None), (7, 8, 6))


def successors(state):
    successors = []
    row, col = next((r, c) for r, row in enumerate(state) for c, value in enumerate(row) if value is None)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = list(list(row) for row in state)
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            successors.append(tuple(tuple(row) for row in new_state))
    return successors


path = bidirectional_search(start_state, goal_state, successors)


if path:
    print("path oldlo")
    print(path)
else:
    print(err)
