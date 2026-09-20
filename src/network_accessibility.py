import math
import networkx as nx
import osmnx as ox
import pandas as pd

def add_walk_time(graph, walking_speed_kph=5.0):
    G = graph.copy()
    speed_mps = walking_speed_kph * 1000 / 3600
    for _, _, _, data in G.edges(keys=True, data=True):
        length = float(data.get("length", 0))
        data["travel_time_s"] = length / speed_mps if speed_mps else math.inf
    return G

def nearest_nodes(graph, gdf):
    if gdf.empty:
        return []
    return list(ox.distance.nearest_nodes(graph, X=gdf.geometry.x.tolist(), Y=gdf.geometry.y.tolist()))

def service_nodes(graph, service_gdf):
    return nearest_nodes(graph, service_gdf)

def multi_source_service_times(graph, destination_nodes):
    destinations = list(dict.fromkeys(destination_nodes))
    if not destinations:
        return {}
    return nx.multi_source_dijkstra_path_length(graph, destinations, weight="travel_time_s")

def accessibility_from_origins(graph, origins_gdf, service_gdf):
    distances = multi_source_service_times(graph, service_nodes(graph, service_gdf))
    origin_nodes = nearest_nodes(graph, origins_gdf)
    rows = []
    for i, node in enumerate(origin_nodes):
        seconds = distances.get(node, math.inf)
        rows.append({
            "origin_index": origins_gdf.index[i],
            "network_node": node,
            "travel_time_s": seconds,
            "travel_time_min": seconds / 60 if math.isfinite(seconds) else math.inf,
        })
    return pd.DataFrame(rows)

def threshold_coverage(accessibility_df, thresholds=(5, 10, 15)):
    values = accessibility_df["travel_time_min"]
    rows = []
    for threshold in thresholds:
        reached = int((values <= threshold).sum())
        rows.append({
            "threshold_min": threshold,
            "origins": len(values),
            "reached": reached,
            "coverage_pct": 100 * reached / len(values) if len(values) else 0,
        })
    return pd.DataFrame(rows)
