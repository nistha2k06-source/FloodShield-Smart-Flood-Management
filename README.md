# FloodShield – Smart Flood Management System

## About the Project
FloodShield is a Python-based mini project developed for the Design and Analysis of Algorithms (DAA) subject. It demonstrates how graph algorithms can help in flood emergency planning by finding safe routes, identifying nearby shelters, and analysing flood risk areas.

## Features
- **Safe Route Finding:** Uses Dijkstra's Algorithm to find the shortest safe route while avoiding flooded roads.
- **Nearest Shelter:** Uses Breadth-First Search (BFS) to identify the nearest reachable shelter.
- **Flood Risk Analysis:** Uses a Priority Queue to arrange areas according to their risk levels.
- **Road Network Visualisation:** Displays locations, safe roads, and flooded roads using Matplotlib.
- **Interactive Dashboard:** Provides a user-friendly graphical interface.

## Technologies Used
- Python 3.14.7
- Tkinter
- CustomTkinter
- NetworkX
- Matplotlib

## Project Structure
```text
FloodShield/
│
├── main.py
├── algorithms.py
├── graph_data.py

```

## Algorithms Implemented

| Algorithm | Purpose |
|---|---|
| Dijkstra's Algorithm | Shortest safe route |
| BFS | Nearest safe shelter |
| Priority Queue | Flood risk prioritisation |

## Installation and Execution

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/FloodShield-Smart-Flood-Management.git
```

2. Open the project folder:
```bash
cd FloodShield-Smart-Flood-Management
```

3. Install required libraries:
```bash
pip install customtkinter networkx matplotlib
```

4. Run the application:
```bash
python main.py
```

## Sample Output
The application demonstrates:
- Safe route from A to F: A → C → D → F
- Total route distance: 8 units
- Nearest safe shelter: F
- Flood risk analysis in descending order

## Limitations
- Uses sample flood and road data.
- Does not provide real-time flood monitoring.
- Does not include live GPS tracking.

## Future Scope
- Real-time weather and flood data integration.
- GPS-based location tracking.
- Emergency alerts and notifications.
- Live map integration.

.
