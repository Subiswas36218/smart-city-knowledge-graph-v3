import osmnx as ox
import pandas as pd
import geopandas as gpd

SERVICE_TAGS = {
    "hospital": {"amenity": "hospital"},
    "pharmacy": {"amenity": "pharmacy"},
    "school": {"amenity": "school"},
    "university": {"amenity": "university"},
    "supermarket": {"shop": "supermarket"},
    "train_station": {"railway": "station"},
    "bus_stop": {"highway": "bus_stop"},
    "library": {"amenity": "library"},
    "park": {"leisure": "park"},
    "bank": {"amenity": "bank"},
    "atm": {"amenity": "atm"},
}

TRANSPORT_TAGS = {
    "bus_stop": {"highway": "bus_stop"},
    "rail_station": {"railway": "station"},
    "tram_stop": {"railway": "tram_stop"},
    "subway_entrance": {"railway": "subway_entrance"},
}

def fetch_pois(city_name):
    polygon = ox.geocode_to_gdf(city_name).geometry.iloc[0]
    frames = []
    for service, tags in SERVICE_TAGS.items():
        try:
            gdf = ox.features_from_polygon(polygon, tags)
        except Exception:
            continue
        if len(gdf):
            gdf = gdf.reset_index()
            gdf["service_type"] = service
            frames.append(gdf)
    if not frames:
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")
    return gpd.GeoDataFrame(pd.concat(frames, ignore_index=True), crs=frames[0].crs)

def fetch_buildings(city_name):
    polygon = ox.geocode_to_gdf(city_name).geometry.iloc[0]
    return ox.features_from_polygon(polygon, {"building": True}).reset_index()

def fetch_roads(city_name):
    graph = ox.graph_from_place(
        city_name,
        network_type="drive",
        simplify=True,
    )

    _, edges = ox.graph_to_gdfs(graph)

    edges = edges.reset_index()

    # Normalize OSM IDs because OSMnx may store them as either
    # integers or lists of integers.
    if "osmid" in edges.columns:
        edges["osmid"] = edges["osmid"].map(
            lambda value: (
                ", ".join(map(str, value))
                if isinstance(value, (list, tuple, set))
                else str(value)
            )
        )

    edges["road_id"] = edges.apply(
        lambda row: f"{row['u']}_{row['v']}_{row['key']}",
        axis=1,
    )

    return edges

def fetch_transport(city_name):
    polygon = ox.geocode_to_gdf(city_name).geometry.iloc[0]
    frames = []
    for transport_type, tags in TRANSPORT_TAGS.items():
        try:
            gdf = ox.features_from_polygon(polygon, tags)
        except Exception:
            continue
        if len(gdf):
            gdf = gdf.reset_index()
            gdf["transport_type"] = transport_type
            frames.append(gdf)
    if not frames:
        return gpd.GeoDataFrame(geometry=[], crs="EPSG:4326")
    return gpd.GeoDataFrame(pd.concat(frames, ignore_index=True), crs=frames[0].crs)

def fetch_walk_network(city_name):
    return ox.graph_from_place(city_name, network_type="walk", simplify=True)

from pathlib import Path
import pandas as pd


from pathlib import Path
import json
import pandas as pd


def _serialize_osm_value(value):
    """Safely normalize heterogeneous OSM attribute values."""

    if value is None:
        return None

    if isinstance(value, (list, tuple, set)):
        return json.dumps(
            list(value),
            ensure_ascii=False,
            default=str,
        )

    if isinstance(value, dict):
        return json.dumps(
            value,
            ensure_ascii=False,
            default=str,
        )

    try:
        if pd.isna(value):
            return None
    except (TypeError, ValueError):
        pass

    return str(value)


def save_geodata(gdf, path):
    """Save an OSM GeoDataFrame safely to GeoParquet."""

    gdf = gdf.copy()

    geometry_column = gdf.geometry.name

    for column in gdf.columns:

        if column == geometry_column:
            continue

        if gdf[column].dtype == "object":
            gdf[column] = gdf[column].map(
                _serialize_osm_value
            )

    Path(path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    gdf.to_parquet(
        path,
        engine="pyarrow",
        index=False,
    )
