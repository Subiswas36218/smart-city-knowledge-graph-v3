import geopandas as gpd
import pandas as pd

def representative_points(gdf):
    if gdf.empty:
        return gdf.copy()
    work = gdf.to_crs(25832)
    work["geometry"] = work.geometry.representative_point()
    return work.to_crs(4326)

def clean_pois(gdf):
    gdf = gdf[gdf.geometry.notna()].drop_duplicates().copy()
    gdf = representative_points(gdf)
    if "name" not in gdf.columns:
        gdf["name"] = "Unnamed"
    else:
        gdf["name"] = gdf["name"].fillna("Unnamed")
    return gdf

def clean_buildings(gdf):
    return gdf[gdf.geometry.notna()].drop_duplicates().to_crs(4326)

def clean_roads(gdf):
    return gdf[gdf.geometry.notna()].drop_duplicates().to_crs(4326)

def clean_transport(gdf):
    return representative_points(gdf)

def service_summary(gdf):
    if gdf.empty or "service_type" not in gdf.columns:
        return pd.DataFrame(columns=["service_type", "count"])
    return gdf.groupby("service_type").size().reset_index(name="count").sort_values("count", ascending=False)
