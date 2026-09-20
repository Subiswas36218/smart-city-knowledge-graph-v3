import requests
import pandas as pd

ENDPOINT = "https://query.wikidata.org/sparql"

def extract_wikidata_ids(gdf):
    ids = set()
    for col in ("wikidata", "brand:wikidata", "operator:wikidata"):
        if col in gdf.columns:
            for value in gdf[col].dropna().astype(str):
                for token in value.replace(";", ",").split(","):
                    token = token.strip()
                    if token.startswith("Q") and token[1:].isdigit():
                        ids.add(token)
    return sorted(ids)

def query_wikidata(entity_ids, user_agent, timeout=45):
    if not entity_ids:
        return pd.DataFrame()
    values = " ".join(f"wd:{qid}" for qid in dict.fromkeys(entity_ids))
    query = f'''
    SELECT ?item ?itemLabel ?description ?type ?typeLabel ?website ?lat ?lon WHERE {{
      VALUES ?item {{ {values} }}
      OPTIONAL {{ ?item wdt:P31 ?type. }}
      OPTIONAL {{ ?item schema:description ?description. FILTER(LANG(?description)="en") }}
      OPTIONAL {{ ?item wdt:P856 ?website. }}
      OPTIONAL {{
        ?item p:P625 ?statement.
        ?statement psv:P625 ?coord.
        ?coord wikibase:geoLatitude ?lat.
        ?coord wikibase:geoLongitude ?lon.
      }}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en,de". }}
    }}
    '''
    r = requests.get(
        ENDPOINT,
        params={"query": query, "format": "json"},
        headers={"Accept": "application/sparql-results+json", "User-Agent": user_agent},
        timeout=timeout,
    )
    r.raise_for_status()
    rows = []
    for b in r.json()["results"]["bindings"]:
        rows.append({
            "wikidata_id": b["item"]["value"].rsplit("/", 1)[-1],
            "label": b.get("itemLabel", {}).get("value"),
            "description": b.get("description", {}).get("value"),
            "type_id": b.get("type", {}).get("value", "").rsplit("/", 1)[-1] or None,
            "type_label": b.get("typeLabel", {}).get("value"),
            "website": b.get("website", {}).get("value"),
            "lat": b.get("lat", {}).get("value"),
            "lon": b.get("lon", {}).get("value"),
        })
    return pd.DataFrame(rows).drop_duplicates()

def enrich_osm_with_wikidata(gdf, user_agent, max_entities=100):
    ids = extract_wikidata_ids(gdf)[:max_entities]
    wd = query_wikidata(ids, user_agent)
    out = gdf.copy()
    if "wikidata" not in out.columns:
        out["wikidata"] = None
    out["wikidata_id"] = out["wikidata"].astype("string").str.extract(r"(Q\d+)", expand=False)
    if not wd.empty:
        out = out.merge(wd, on="wikidata_id", how="left")
    return out, wd
