import networkx as nx
import osmnx as ox

def network_summary(graph):
    return {"nodes": graph.number_of_nodes(), "edges": graph.number_of_edges(), "density": nx.density(graph)}

def sampled_betweenness(graph, sample_size=300):
    G = ox.convert.to_undirected(graph)
    k = min(sample_size, len(G))
    return nx.betweenness_centrality(G, k=k, normalized=True, seed=42) if k else {}
