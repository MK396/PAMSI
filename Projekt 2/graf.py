import networkx as nx
import matplotlib.pyplot as plt

# 1. Definicja stanów
nodes = {
    "S1": "Rozpoczęcie\nsesji",
    "S2": "Wyświetlenie\nproduktu",
    "S3": "Dodanie do\nkoszyka",
    "S4": "Proces\npłatności",
    "S5": "Zakup",
    "E": "EXIT"
}

G = nx.DiGraph()

# 2. Dane krawędzi
edges = [
    ("S1", "S2", "16.5%"), ("S2", "S3", "24.3%"),
    ("S3", "S4", "52.1%"), ("S4", "S5", "51.7%"),
    ("S1", "E", "83.5%"), ("S2", "E", "75.7%"),
    ("S3", "E", "47.9%"), ("S4", "E", "48.3%")
]

for u, v, label in edges:
    G.add_edge(u, v, label=label)

# Definicje przepływów
main_flow = [("S1", "S2"), ("S2", "S3"), ("S3", "S4"), ("S4", "S5")]
exit_flow = [("S1", "E"), ("S2", "E"), ("S3", "E"), ("S4", "E")]

# 3. Pozycjonowanie
pos = {
    "S1": (0, 2), 
    "S2": (5, 2), 
    "S3": (10, 2), 
    "S4": (15, 2), 
    "S5": (20, 2),
    "E": (10, -0.5) 
}

plt.figure(figsize=(18, 10))

# 4. Rysowanie węzłów
node_colors = []
for node in G.nodes():
    if node == "S5": node_colors.append('lightgreen')
    elif node == "E": node_colors.append('salmon')
    else: node_colors.append('lightblue')

nx.draw_networkx_nodes(G, pos, node_size=7000, edgecolors='black', node_color=node_colors)
nx.draw_networkx_labels(G, pos, labels=nodes, font_size=11, font_weight='bold')

# 5. Rysowanie krawędzi
nx.draw_networkx_edges(G, pos, edgelist=main_flow, arrowsize=35, edge_color='royalblue', width=3)
nx.draw_networkx_edges(G, pos, edgelist=exit_flow, arrowsize=25, edge_color='crimson', 
                       style='dashed', alpha=0.7, connectionstyle="arc3,rad=0.15")

# 6. Etykiety krawędzi
edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_weight='bold',
                             bbox=dict(facecolor='white', edgecolor='gray', alpha=0.9, boxstyle='round,pad=0.3'))

plt.title("Customer Behavior Model Graph (CBMG) - Google Merch Shop", 
          fontsize=22, fontweight='bold', y=0.92) 

plt.xlim(-3, 23)
plt.ylim(-1.5, 3.5) 

plt.axis('off')
plt.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.1)

plt.show()