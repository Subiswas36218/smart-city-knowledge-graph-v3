import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

def build_profile_matrix(accessibility_by_service):
    series = {}
    for service, frame in accessibility_by_service.items():
        series[service] = frame.set_index("origin_index")["travel_time_min"]
    return pd.DataFrame(series).replace([float("inf")], pd.NA).fillna(999.0)

def cluster_kmeans(profile, k=4):
    X = StandardScaler().fit_transform(profile)
    labels = KMeans(n_clusters=k, random_state=42, n_init=20).fit_predict(X)
    metrics = {"algorithm":"KMeans","k":k}
    if len(set(labels)) > 1:
        metrics["silhouette"] = silhouette_score(X, labels)
        metrics["davies_bouldin"] = davies_bouldin_score(X, labels)
        metrics["calinski_harabasz"] = calinski_harabasz_score(X, labels)
    return labels, metrics

def cluster_dbscan(profile, eps=0.8, min_samples=8):
    X = StandardScaler().fit_transform(profile)
    labels = DBSCAN(eps=eps, min_samples=min_samples).fit_predict(X)
    mask = labels != -1
    metrics = {"algorithm":"DBSCAN","eps":eps,"min_samples":min_samples}
    if mask.sum() > 2 and len(set(labels[mask])) > 1:
        metrics["silhouette"] = silhouette_score(X[mask], labels[mask])
        metrics["davies_bouldin"] = davies_bouldin_score(X[mask], labels[mask])
        metrics["calinski_harabasz"] = calinski_harabasz_score(X[mask], labels[mask])
    return labels, metrics

def cluster_profiles(profile, labels):
    out = profile.copy(); out["cluster"] = labels
    return out.groupby("cluster").mean(numeric_only=True)
