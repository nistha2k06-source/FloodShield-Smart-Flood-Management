
import networkx as nx

G = nx.Graph()

locations = {
    "A": "City Center",
    "B": "North Area",
    "C": "East Area",
    "D": "South Area",
    "E": "West Area",
    "F": "Safe Shelter"
}

roads = [
    ("A", "B", 4, 0),
    ("A", "C", 3, 0),
    ("B", "D", 5, 1),
    ("C", "D", 2, 0),
    ("C", "E", 4, 0),
    ("D", "F", 3, 0),
    ("E", "F", 2, 0),
    ("B", "E", 6, 1)
]

for u, v, distance, flood in roads:
    G.add_edge(u, v, weight=distance, flooded=flood)

safe_locations = ["F"]

