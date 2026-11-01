
import customtkinter as ctk
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import messagebox

from graph_data import G, locations, safe_locations
from algorithms import find_safe_route, find_nearby_shelter, get_high_risk_areas

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("FloodShield | Smart Flood Management")
app.geometry("1100x720")
app.configure(fg_color="#F3F6FA")

NAVY = "#172D4B"
TEAL = "#078C91"
WHITE = "#FFFFFF"
GRAY = "#718096"

# Sidebar
side = ctk.CTkFrame(app, width=205, fg_color=NAVY, corner_radius=0)
side.pack(side="left", fill="y")
side.pack_propagate(False)

ctk.CTkLabel(side, text="🌊 FloodShield",
             font=("Arial", 23, "bold"),
             text_color="#62DFC9").pack(pady=(35, 5))

ctk.CTkLabel(side, text="EMERGENCY MANAGEMENT",
             font=("Arial", 10),
             text_color="#B8C9D9").pack(pady=(0, 35))

for item in ["▣  Dashboard", "⌖  Safe Routes",
             "⌂  Shelters", "▤  Risk Analysis", "◎  Road Network"]:
    ctk.CTkLabel(side, text=item, font=("Arial", 14),
                 text_color="white").pack(anchor="w", padx=22, pady=18)

ctk.CTkLabel(side, text="STAY ALERT.\nSTAY SAFE.",
             font=("Arial", 15, "bold"),
             text_color="#62DFC9").pack(side="bottom", pady=35)

# Main Dashboard
main = ctk.CTkScrollableFrame(app, fg_color="#F3F6FA")
main.pack(side="left", fill="both", expand=True, padx=22, pady=20)

ctk.CTkLabel(main, text="Flood Monitoring Dashboard",
             font=("Arial", 27, "bold"),
             text_color=NAVY).pack(anchor="w")

ctk.CTkLabel(main, text="Smart emergency route and shelter management",
             font=("Arial", 13), text_color=GRAY).pack(anchor="w", pady=5)

# Welcome Banner
banner = ctk.CTkFrame(main, fg_color=NAVY, corner_radius=16)
banner.pack(fill="x", pady=20)

ctk.CTkLabel(banner, text="SMART FLOOD MANAGEMENT",
             text_color="#62DFC9",
             font=("Arial", 11, "bold")).pack(anchor="w", padx=25, pady=(22, 5))

ctk.CTkLabel(banner, text="Stay Safe. Find Your Way.",
             text_color=WHITE,
             font=("Arial", 27, "bold")).pack(anchor="w", padx=25)

ctk.CTkLabel(banner, text="Intelligent solutions for safer communities.",
             text_color="#D5E3ED").pack(anchor="w", padx=25, pady=(5, 22))

# Statistics Cards
cards = ctk.CTkFrame(main, fg_color="transparent")
cards.pack(fill="x", pady=5)

for title, value, color in [
    ("🌊 Flood Zones", "04", "#E15B5B"),
    ("🏠 Safe Shelters", "01", TEAL),
    ("🚧 Blocked Roads", "02", "#D58A32"),
    ("✓ System Status", "ACTIVE", "#179B72")
]:
    card = ctk.CTkFrame(cards, fg_color=WHITE, corner_radius=14)
    card.pack(side="left", expand=True, fill="x", padx=5)

    ctk.CTkLabel(card, text=title, text_color=GRAY,
                 font=("Arial", 12)).pack(pady=(17, 7))

    ctk.CTkLabel(card, text=value, text_color=color,
                 font=("Arial", 22, "bold")).pack(pady=(0, 17))

# Input Panel
panel = ctk.CTkFrame(main, fg_color=WHITE, corner_radius=15)
panel.pack(fill="x", pady=20)

ctk.CTkLabel(panel, text="Emergency Route Planner",
             font=("Arial", 20, "bold"),
             text_color=NAVY).pack(anchor="w", padx=20, pady=15)

inputs = ctk.CTkFrame(panel, fg_color="transparent")
inputs.pack(fill="x", padx=15)

start = ctk.CTkOptionMenu(inputs, values=list(locations.keys()),
                          fg_color=NAVY, button_color=TEAL)
start.set("A")
start.pack(side="left", expand=True, padx=8, pady=8)

end = ctk.CTkOptionMenu(inputs, values=list(locations.keys()),
                        fg_color=NAVY, button_color=TEAL)
end.set("F")
end.pack(side="left", expand=True, padx=8, pady=8)

result = ctk.CTkLabel(panel, text="Your results will appear here",
                      text_color=TEAL, font=("Arial", 13),
                      wraplength=650)
result.pack(pady=12)

# Algorithms
def route():
    if start.get() == end.get():
        result.configure(text="Choose two different locations.")
        return

    path, distance = find_safe_route(G, start.get(), end.get())
    if path:
        names = " → ".join(locations[x] for x in path)
        result.configure(text=f"SAFE ROUTE: {names}   |   Distance: {distance} units")
    else:
        result.configure(text="No safe route available.")

def shelter():
    found = find_nearby_shelter(G, start.get(), safe_locations)
    result.configure(text=f"Nearest Shelter: {locations[found]}" if found
                      else "No reachable shelter found.")

def risk():
    data = {"North Area": 90, "South Area": 80,
            "East Area": 60, "West Area": 40}
    values = get_high_risk_areas(data)
    result.configure(text="   |   ".join(f"{n}: {v}%" for n, v in values))


def graph():
    pos = {
        "A": (0, 2),
        "B": (1, 3),
        "C": (2, 2),
        "D": (3, 3),
        "E": (3, 1),
        "F": (4, 2)
    }

    fig, ax = plt.subplots(figsize=(9, 5))
    fig.patch.set_facecolor("#F3F6FA")
    ax.set_facecolor("#FFFFFF")

    nx.draw_networkx_edges(
        G, pos, ax=ax, width=3,
        edge_color=[
            "#E45757" if G[u][v]["flooded"] else "#078C91"
            for u, v in G.edges()
        ]
    )

    nx.draw_networkx_nodes(
        G, pos, ax=ax, node_size=2300,
        node_color="#D9F3F0",
        edgecolors="#078C91", linewidths=2
    )

    nx.draw_networkx_labels(
        G, pos, ax=ax,
        labels=locations, font_size=9,
        font_weight="bold", font_color="#172D4B"
    )

    nx.draw_networkx_edge_labels(
        G, pos, ax=ax,
        edge_labels=nx.get_edge_attributes(G, "weight"),
        font_size=10, font_color="#172D4B",
        label_pos=0.5, rotate=False
    )

    ax.set_title(
        "FLOODSHIELD | ROAD NETWORK",
        fontsize=15, fontweight="bold",
        color="#172D4B", pad=20
    )

    ax.text(
        0.02, 0.02,
        "● Safe Road     ● Flooded Road",
        transform=ax.transAxes,
        fontsize=10, color="#172D4B"
    )

    ax.axis("off")
    plt.tight_layout()
    plt.show()


# Action Buttons
actions = ctk.CTkFrame(main, fg_color="transparent")
actions.pack(fill="x", pady=5)

for name, command in [
    ("Find Safe Route", route),
    ("Find Shelter", shelter),
    ("Analyze Risk", risk),
    ("View Road Graph", graph)
]:
    ctk.CTkButton(actions, text=name, command=command,
                  fg_color=TEAL, hover_color="#066D73",
                  height=40, corner_radius=9).pack(
                      fill="x", pady=5, padx=5)

ctk.CTkLabel(main, text="FloodShield | DAA Mini Project",
             text_color=GRAY).pack(pady=15)

app.mainloop()

