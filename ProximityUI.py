import matplotlib.pyplot as plt
import networkx as nx

# Create a network graph from the co-occurrence data
G = nx.Graph()

# Add nodes and edges to the graph
for word, counter in co_occurrence.items():
    for co_word, count in counter.items():
        if count > 1:  # Only include edges with significant co-occurrence
            G.add_edge(word, co_word, weight=count)

# Position the nodes using a layout algorithm
pos = nx.spring_layout(G, k=0.5, iterations=50)

# Draw the network graph
plt.figure(figsize=(12, 8))

# Draw the nodes with size proportional to their degree (number of connections)
node_sizes = [1000 * G.degree(node) for node in G]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='lightblue', alpha=0.7)

# Draw edges with thickness proportional to their weight (co-occurrence frequency)
edge_widths = [G[u][v]['weight'] for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.5)

# Draw the node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Draw the edge labels (optional, can be removed if the graph is too cluttered)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# Display the graph
plt.title("Proximity Analysis Network Graph")
plt.show()
