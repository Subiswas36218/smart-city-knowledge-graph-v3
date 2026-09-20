import pandas as pd

def spatial_coverage_report(gdf, label_column):
    if gdf.empty or label_column not in gdf.columns:
        return pd.DataFrame()
    return gdf[label_column].value_counts(dropna=False).rename_axis(label_column).reset_index(name="count")

def accessibility_summary(df):
    v = pd.to_numeric(df["travel_time_min"], errors="coerce").replace([float("inf"), -float("inf")], pd.NA).dropna()
    if v.empty: return {}
    return {"count": int(v.count()), "mean_min": float(v.mean()), "median_min": float(v.median()), "p90_min": float(v.quantile(.9))}
