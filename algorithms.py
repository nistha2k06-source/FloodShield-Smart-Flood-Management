
import networkx as nx
from collections import deque
import heapq

# Dijkstra: Find Safe Route
def find_safe_route(G, start, end):
    H = G.copy()

    for u, v, d in list(H.edges(data=True)):
        if d["flooded"]:
            H.remove_edge(u, v)

    try:
        path = nx.dijkstra_path(H, start, end, weight="weight")
        distance = nx.dijkstra_path_length(H, start, end, weight="weight")
        return path, distance
    except nx.NetworkXNoPath:
        return [], 0

# BFS: Find Nearest Safe Shelter
def find_nearby_shelter(G, start, shelters):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()

        if node in shelters:
            return node

        for n in G.neighbors(node):
            if n not in visited and not G[node][n]["flooded"]:
                visited.add(n)
                queue.append(n)

    return None

# Priority Queue: Risk Analysis
def get_high_risk_areas(data):
    heap = []

    for name, risk in data.items():
        heapq.heappush(heap, (-risk, name))

    return [ (name, -risk) for risk, name in
             [heapq.heappop(heap) for _ in range(len(heap))] ]

