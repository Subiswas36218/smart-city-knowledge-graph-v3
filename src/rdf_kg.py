from pathlib import Path
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, OWL

SC = Namespace("https://example.org/smartcity/")
EX = Namespace("https://example.org/entity/")
GEO = Namespace("http://www.opengis.net/ont/geosparql#")

def make_graph():
    g = Graph()
    g.bind("sc", SC); g.bind("ex", EX); g.bind("geo", GEO); g.bind("owl", OWL)
    return g

def safe_uri(prefix, value):
    return EX[f"{prefix}_{str(value).replace(' ', '_').replace('/', '_').replace(':', '_')}"]

def add_geometry(g, subject, geometry):
    if geometry is None or geometry.is_empty:
        return
    geom = URIRef(f"{subject}/geometry")
    g.add((subject, GEO.hasGeometry, geom))
    g.add((geom, RDF.type, GEO.Geometry))
    g.add((geom, GEO.asWKT, Literal(geometry.wkt, datatype=GEO.wktLiteral)))

def add_feature(g, row, feature_type, index):
    subject = safe_uri(feature_type.lower(), row.get("osmid", row.get("id", index)))
    g.add((subject, RDF.type, SC[feature_type]))
    if row.get("name") and str(row["name"]) != "nan":
        g.add((subject, RDFS.label, Literal(str(row["name"]))))
    if row.get("service_type") and str(row["service_type"]) != "nan":
        g.add((subject, SC.serviceType, Literal(str(row["service_type"]))))
    if row.get("transport_type") and str(row["transport_type"]) != "nan":
        g.add((subject, SC.transportType, Literal(str(row["transport_type"]))))
    qid = row.get("wikidata_id")
    if qid and str(qid) != "nan":
        wd = URIRef(f"https://www.wikidata.org/entity/{qid}")
        g.add((subject, OWL.sameAs, wd))
        for key, pred in [("label", RDFS.label), ("description", SC.description)]:
            if row.get(key) and str(row[key]) != "nan":
                g.add((wd, pred, Literal(str(row[key]))))
        if row.get("website") and str(row["website"]) != "nan":
            g.add((wd, SC.officialWebsite, URIRef(str(row["website"]))))
    add_geometry(g, subject, row.get("geometry"))

def build_knowledge_graph(pois=None, buildings=None, roads=None, transport=None):
    g = make_graph()
    for frame, kind in ((pois, "POI"), (buildings, "Building"), (roads, "Road"), (transport, "Transport")):
        if frame is not None and not frame.empty:
            for i, (_, row) in enumerate(frame.iterrows()):
                add_feature(g, row, kind, i)
    return g

def save_graph(g, turtle_path, jsonld_path):
    Path(turtle_path).parent.mkdir(parents=True, exist_ok=True)
    g.serialize(destination=turtle_path, format="turtle")
    Path(jsonld_path).write_text(g.serialize(format="json-ld", indent=2), encoding="utf-8")

def kg_to_networkx(g):
    import networkx as nx
    G = nx.MultiDiGraph()
    for s, p, o in g:
        G.add_node(str(s)); G.add_node(str(o))
        G.add_edge(str(s), str(o), predicate=str(p))
    return G
