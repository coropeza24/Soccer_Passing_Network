import networkx as nx
import matplotlib.pyplot as plt

''' Step 1: Define players in a 4-3-3 formation '''
players = [
    "GK", "LB", "CB1", "CB2", "RB",
    "LM", "CM", "RM",
    "LW", "ST", "RW"
]

''' Step 2: Define possible passes (edges) '''
passes = [
    ("GK", "CB1"), ("GK", "CB2"),
    ("CB1", "LB"), ("CB2", "RB"),
    ("CB1", "CM"), ("CB2", "CM"),
    ("LB", "LM"), ("RB", "RM"),
    ("LM", "CM"), ("CM", "RM"),
    ("LM", "LW"), ("RM", "RW"),
    ("CM", "ST"),
    ("LW", "ST"), ("RW", "ST")
]

''' Step 3: Create graph '''
G = nx.Graph()
G.add_nodes_from(players)
G.add_edges_from(passes)

''' Step 4: Calculate number of passing options '''
print("Passing options per player:")
for player in G.nodes:
    print(f"{player}: {len(list(G.neighbors(player)))} options")

''' Step 5: Calculate centrality (who connects the most) '''
centrality = nx.degree_centrality(G)
most_influential = max(centrality, key=centrality.get)
print(f"\nMost influential player (based on centrality): {most_influential}")

''' Step 6: Visualize formation '''
pos = {
    "GK": (0, 0),
    "LB": (-3, 2), "CB1": (-1, 2), "CB2": (1, 2), "RB": (3, 2),
    "LM": (-2, 4), "CM": (0, 4), "RM": (2, 4),
    "LW": (-2, 6), "ST": (0, 6), "RW": (2, 6)
}

plt.figure(figsize=(8,6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1800, font_size=10)
nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')
plt.title("⚽ Soccer Passing Network (4-3-3 Formation)")
plt.show()
