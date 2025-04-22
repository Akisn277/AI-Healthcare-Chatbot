import heapq

class Node:
    def __init__(self, name, cost=0, heuristic=0, parent=None):
        self.name = name
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]

def a_star_search(start, goal, graph, heuristics):
    open_list = []
    heapq.heappush(open_list, Node(start, heuristic=heuristics[start]))
    closed = set()

    while open_list:
        current = heapq.heappop(open_list)

        if current.name == goal:
            return reconstruct_path(current)

        closed.add(current.name)

        for neighbor, cost in graph.get(current.name, []):
            if neighbor not in closed:
                heapq.heappush(open_list, Node(neighbor, current.cost + cost, heuristics.get(neighbor, 0), current))

    return None

graph = {
    "start": [("fever", 1), ("headache", 2), ("cough", 1)],
    "fever": [("fatigue", 1), ("flu", 2)],
    "headache": [("covid", 2)],
    "cough": [("cold", 1), ("covid", 2)],
    "fatigue": [("flu", 1)],
    "cold": [],
    "covid": [],
    "flu": []
}

heuristics = {
    "start": 3,
    "fever": 2,
    "headache": 2,
    "cough": 2,
    "fatigue": 1,
    "flu": 0,
    "covid": 0,
    "cold": 0
}
