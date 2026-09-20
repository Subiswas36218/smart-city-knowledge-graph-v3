# 🏙️ Smart City Knowledge Graph & Network Accessibility Analyzer

[![CI](https://github.com/Subiswas36218/smart-city-knowledge-graph-v3.git/actions/workflows/ci.yml/badge.svg)](https://github.com/Subiswas36218/smart-city-knowledge-graph-v3.git/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![GeoPandas](https://img.shields.io/badge/GeoPandas-Geospatial-139C5A)](https://geopandas.org/)
[![OSMnx](https://img.shields.io/badge/OSMnx-OpenStreetMap-3B82F6)](https://osmnx.readthedocs.io/)
[![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-Data-7EBC6F?logo=openstreetmap&logoColor=white)](https://www.openstreetmap.org/)
[![Wikidata](https://img.shields.io/badge/Wikidata-Enrichment-990000?logo=wikidata&logoColor=white)](https://www.wikidata.org/)
[![RDFLib](https://img.shields.io/badge/RDFLib-RDF%2FSPARQL-6B4FBB)](https://rdflib.readthedocs.io/)
[![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20Analytics-F47C20)](https://networkx.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/python/)
[![Folium](https://img.shields.io/badge/Folium-Interactive%20Maps-77B829)](https://python-visualization.github.io/folium/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Parquet](https://img.shields.io/badge/Apache%20Parquet-Storage-50ABF1)](https://parquet.apache.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A reproducible geospatial knowledge-graph and network-accessibility pipeline for **Eschwege, Hesse, Germany**, combining OpenStreetMap, Wikidata, RDF/SPARQL, NetworkX, Dijkstra routing, accessibility analysis, clustering, and interactive visualization.

## 📌 Overview

This project transforms heterogeneous urban data into a connected Smart City analytics workflow. It covers the full path from live OpenStreetMap ingestion to semantic enrichment, knowledge-graph construction, pedestrian-network accessibility, machine-learning segmentation, interactive visualization, and reproducibility metadata.

### Core objectives

- Ingest POIs, buildings, roads, and transport data from OpenStreetMap.
- Clean and standardize geospatial datasets.
- Enrich selected OSM entities using Wikidata.
- Build RDF/Turtle and JSON-LD knowledge graphs.
- Query urban entities using SPARQL.
- Calculate walking travel times using a network graph and Dijkstra shortest paths.
- Measure 5/10/15-minute service accessibility.
- Cluster accessibility profiles with KMeans and DBSCAN.
- Produce interactive maps and charts with Folium and Plotly.
- Capture dataset, environment, model, and run metadata.
- Validate the Python codebase through GitHub Actions.

## 🔄 Live End-to-End Workflow

```text
OpenStreetMap ───────────────┐
  POIs                       │
  Buildings                  │
  Roads                      ├──> 01 Live OSM Ingestion
  Transport                  │             │
                             │             ▼
Wikidata ────────────────────┘      02 Geospatial Cleaning
                                           │
                                           ▼
                                  03 Wikidata Enrichment
                                           │
                              ┌────────────┴────────────┐
                              ▼                         ▼
                    04 RDF Knowledge Graph      Walking Network
                    Turtle + JSON-LD                  │
                              │                         ▼
                              ▼               06 Network Accessibility
                    05 SPARQL Queries                  │
                                                        ▼
                                             07 Accessibility Coverage
                                             5 / 10 / 15 minutes
                                                        │
                                                        ▼
                                               08 ML Clustering
                                             KMeans + DBSCAN
                                                        │
                                                        ▼
                                             09 Interactive Dashboard
                                                        │
                                                        ▼
                                             10 Evaluation & Metadata
```

The workflow is intentionally sequential because each stage produces artifacts consumed by later stages.

## 📓 Notebook Pipeline

| Notebook | Stage | Main output |
|---|---|---|
| `01_live_osm_ingestion.ipynb` | Live OSM ingestion | Raw geospatial data + networks |
| `02_geospatial_cleaning.ipynb` | Cleaning | Clean POIs, buildings, roads, transport |
| `03_wikidata_enrichment.ipynb` | Semantic enrichment | `pois_wikidata.parquet` |
| `04_rdf_knowledge_graph.ipynb` | Knowledge graph | Turtle + JSON-LD |
| `05_sparql_queries.ipynb` | Semantic analytics | SPARQL results |
| `06_network_accessibility.ipynb` | Network analysis | Travel-time matrix |
| `07_accessibility_coverage.ipynb` | Accessibility | Threshold coverage |
| `08_ml_clustering.ipynb` | Machine learning | KMeans + DBSCAN profiles |
| `09_dashboard.ipynb` | Visualization | Interactive maps + charts |
| `10_evaluation_and_metadata.ipynb` | Evaluation | Metrics + `run_metadata.json` |

## 🧰 Tech Stack

### Data & geospatial

- [Python](https://www.python.org/) — core language
- [Pandas](https://pandas.pydata.org/) — tabular processing
- [GeoPandas](https://geopandas.org/) — geospatial processing
- [OSMnx](https://osmnx.readthedocs.io/) — OpenStreetMap extraction and networks
- [Shapely](https://shapely.readthedocs.io/) — geometry operations
- [PyArrow](https://arrow.apache.org/docs/python/) — Parquet I/O
- [Apache Parquet](https://parquet.apache.org/) — columnar storage

### Knowledge graph & semantic web

- [RDFLib](https://rdflib.readthedocs.io/) — RDF graph construction
- [SPARQL 1.1](https://www.w3.org/TR/sparql11-query/) — semantic queries
- [W3C RDF](https://www.w3.org/RDF/) — RDF data model
- [Wikidata](https://www.wikidata.org/) — entity enrichment
- [GeoSPARQL](https://opengeospatial.github.io/ogc-geosparql/) — geospatial semantics
- JSON-LD — linked-data serialization

### Network analysis & ML

- [NetworkX](https://networkx.org/) — graph analysis
- Dijkstra shortest path — walking travel time
- [scikit-learn](https://scikit-learn.org/) — clustering and evaluation
- KMeans — accessibility segmentation
- DBSCAN — density-based clustering and noise detection
- Silhouette metrics — cluster evaluation

### Visualization

- [Folium](https://python-visualization.github.io/folium/) — interactive maps
- [Plotly](https://plotly.com/python/) — interactive charts
- [Matplotlib](https://matplotlib.org/) — report-ready static figures
- [Jupyter](https://jupyter.org/) — reproducible notebooks

### Engineering & CI

- [Git](https://git-scm.com/) — version control
- [GitHub](https://github.com/) — collaboration and source hosting
- [GitHub Actions](https://github.com/features/actions) — continuous integration
- Ruff — linting and formatting
- pytest — automated tests

## 📂 Project Structure

```text
smart-city-knowledge-graph-v3/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
│   ├── raw/
│   │   ├── pois_raw.parquet
│   │   ├── buildings_raw.parquet
│   │   ├── roads_raw.parquet
│   │   ├── transport_raw.parquet
│   │   ├── walk_network.graphml
│   │   └── drive_network.graphml
│   └── processed/
│       ├── pois_clean.parquet
│       ├── pois_wikidata.parquet
│       ├── buildings_clean.parquet
│       ├── roads_clean.parquet
│       ├── transport_clean.parquet
│       ├── network_accessibility.csv
│       ├── accessibility_coverage.csv
│       ├── accessibility_profiles.csv
│       ├── cluster_profiles.csv
│       ├── accessibility_profiles_dbscan.csv
│       ├── dbscan_cluster_profiles.csv
│       ├── clustering_metrics.csv
│       └── run_metadata.json
├── notebooks/
│   ├── 01_live_osm_ingestion.ipynb
│   ├── 02_geospatial_cleaning.ipynb
│   ├── 03_wikidata_enrichment.ipynb
│   ├── 04_rdf_knowledge_graph.ipynb
│   ├── 05_sparql_queries.ipynb
│   ├── 06_network_accessibility.ipynb
│   ├── 07_accessibility_coverage.ipynb
│   ├── 08_ml_clustering.ipynb
│   ├── 09_dashboard.ipynb
│   └── 10_evaluation_and_metadata.ipynb
├── outputs/
│   ├── graphs/
│   │   ├── smart_city_kg.ttl
│   │   └── smart_city_kg.jsonld
│   └── maps/
│       ├── poi_map.html
│       ├── travel_time_distribution.html
│       ├── service_travel_time_boxplot.html
│       ├── service_accessibility_bar.html
│       ├── accessibility_heatmap.html
│       ├── accessibility_coverage.html
│       ├── poi_service_distribution.html
│       ├── kmeans_clusters.html
│       ├── dbscan_clusters.html
│       └── cluster_size_comparison.html
├── src/
│   ├── cleaning.py
│   ├── clustering.py
│   ├── config.py
│   ├── kg.py
│   ├── network_accessibility.py
│   ├── visualization.py
│   └── wikidata.py
├── tests/
├── requirements.txt
├── pyproject.toml
└── README.md
```

## 🚀 Installation

### 1. Clone

```bash
git clone https://github.com/Subiswas36218/smart-city-knowledge-graph-v3.git
cd smart-city-knowledge-graph-v3
```

### 2. Create environment

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```powershell
py -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Launch Jupyter

```bash
jupyter lab
```

## ▶️ Run the Pipeline

Run notebooks in order:

```text
01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10
```

For command-line execution with `nbconvert`:

```bash
for notebook in notebooks/*.ipynb; do
  jupyter nbconvert --to notebook --execute "$notebook" \
    --ExecutePreprocessor.timeout=1200 \
    --output "$(basename "$notebook")"
done
```

For normal development, running each notebook interactively is recommended because live OSM/Wikidata stages can require network access and may be affected by external rate limits.

## 🗺️ Interactive Visualizations

Notebook 09 produces browser-based outputs including:

- `poi_map.html` — interactive POI map with service layers
- `poi_service_distribution.html` — interactive service-count chart
- `travel_time_distribution.html` — travel-time histogram and marginal distributions
- `service_accessibility_bar.html` — average accessibility by service
- `service_travel_time_boxplot.html` — distributions and outliers
- `accessibility_heatmap.html` — origin × service travel-time matrix
- `accessibility_coverage.html` — threshold coverage comparison
- `kmeans_clusters.html` — KMeans accessibility clusters
- `dbscan_clusters.html` — DBSCAN accessibility clusters
- `cluster_size_comparison.html` — cluster-size comparison

Open any `.html` file in a browser for interactive exploration.

## 🧠 Knowledge Graph

The RDF graph connects urban entities, services, geometries, and reconciled Wikidata entities.

```text
City
 ├── Building
 ├── POI
 │    ├── Service Type
 │    ├── Geometry
 │    └── owl:sameAs → Wikidata entity
 ├── Road
 └── Transport
```

Generated files:

```text
outputs/graphs/smart_city_kg.ttl
outputs/graphs/smart_city_kg.jsonld
```

Example SPARQL query:

```sparql
PREFIX sc: <https://example.org/smartcity/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?x ?service ?label
WHERE {
    ?x sc:serviceType ?service ;
       rdfs:label ?label .
}
ORDER BY ?service ?label
LIMIT 100
```

## 🚶 Network Accessibility

The walking accessibility workflow is:

```text
Origin POI
   ↓
Nearest network node
   ↓
Walking graph
   ↓
Dijkstra shortest path
   ↓
Target service nodes
   ↓
Travel time in minutes
```

Default origin services:

- school
- university
- supermarket

Default target services:

- hospital
- pharmacy
- supermarket
- train station
- library

Walking speed and origin limits are configurable in `src/config.py`.

## ⏱️ Coverage Analysis

Notebook 07 evaluates service accessibility at configurable thresholds, including the project's 5-, 10-, and 15-minute analysis.

Output:

```text
data/processed/accessibility_coverage.csv
```

## 🤖 Machine Learning

### KMeans

Groups origins according to their multi-service accessibility profiles.

### DBSCAN

Finds dense accessibility patterns and identifies potential noise/outlier origins.

Outputs include:

```text
data/processed/accessibility_profiles.csv
data/processed/cluster_profiles.csv
data/processed/accessibility_profiles_dbscan.csv
data/processed/dbscan_cluster_profiles.csv
data/processed/clustering_metrics.csv
```

## ⚙️ Reproducibility & Evaluation

Notebook 10 generates `data/processed/run_metadata.json`, recording:

- city and project configuration
- walking speed and origin limits
- Python and operating-system information
- package versions
- dataset sizes and CRS
- POI statistics
- RDF triple counts
- Wikidata link counts
- accessibility statistics
- clustering statistics

This makes runs easier to reproduce, compare, and audit.

## 🔁 GitHub Actions / Live CI Workflow

The repository is designed for a lightweight CI workflow that runs on pushes and pull requests:

```text
                 git push / Pull Request
                           │
                           ▼
                  GitHub Actions runner
                           │
                           ▼
                  Checkout repository
                           │
                           ▼
                    Setup Python 3.12
                           │
                           ▼
                  Install requirements
                           │
                           ▼
                    Ruff lint / format
                           │
                           ▼
                       Run pytest
                           │
                           ▼
                    ┌───────────────┐
                    │   CI PASS ✅  │
                    └───────────────┘
```

Suggested `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest ruff

      - name: Ruff lint
        run: ruff check .

      - name: Ruff format check
        run: ruff format --check .

      - name: Tests
        run: pytest
```

GitHub workflow status badges can be placed directly in the README and will reflect the latest workflow state. Replace `OWNER/REPOSITORY` in the badge URL with the actual GitHub repository path.

## 🧪 Local Quality Checks

```bash
ruff check .
ruff format --check .
pytest
```

## 📦 Main Artifacts

| Artifact | Purpose |
|---|---|
| `pois_clean.parquet` | Clean POIs |
| `pois_wikidata.parquet` | Wikidata-enriched POIs |
| `buildings_clean.parquet` | Clean buildings |
| `roads_clean.parquet` | Clean roads |
| `transport_clean.parquet` | Clean transport features |
| `network_accessibility.csv` | Origin-to-service travel times |
| `accessibility_coverage.csv` | Threshold coverage |
| `accessibility_profiles.csv` | KMeans input/assignments |
| `cluster_profiles.csv` | KMeans summaries |
| `accessibility_profiles_dbscan.csv` | DBSCAN assignments |
| `dbscan_cluster_profiles.csv` | DBSCAN summaries |
| `clustering_metrics.csv` | Clustering evaluation |
| `smart_city_kg.ttl` | RDF/Turtle graph |
| `smart_city_kg.jsonld` | JSON-LD graph |
| `run_metadata.json` | Reproducibility metadata |

## 🔐 Data & API Notes

The project uses public OpenStreetMap and Wikidata resources. Live ingestion/enrichment depends on network availability and external service policies. Use a descriptive user agent and reasonable request rates when querying external services.

Large generated datasets should generally not be committed directly to Git. Consider Git LFS, GitHub Releases, or external storage for large artifacts.

## 🏙️ Extending to Another City

The architecture is city-independent. Update the configuration and rerun the notebooks for another location.

Potential extensions:

- 🚲 cycling accessibility
- 🚌 public-transport accessibility
- 🚗 driving accessibility
- 🏥 healthcare accessibility
- 🏫 education accessibility
- 🌳 green-space accessibility
- 🛒 essential-service accessibility
- 🌍 multi-city comparison
- 🗃️ persistent RDF triplestore
- ⚡ real-time urban-data ingestion
- 🧠 graph neural networks
- 🌐 deployed web dashboard

## 📚 Reproducibility Checklist

- [ ] Python 3.12 environment created
- [ ] Dependencies installed
- [ ] Live OSM/Wikidata access available where required
- [ ] Notebook 01 completed
- [ ] Raw datasets and networks generated
- [ ] Notebook 02 completed
- [ ] Wikidata enrichment completed or intentionally disabled
- [ ] RDF/Turtle and JSON-LD generated
- [ ] SPARQL queries executed
- [ ] Network accessibility calculated
- [ ] Coverage metrics generated
- [ ] KMeans and DBSCAN completed
- [ ] Interactive visualizations generated
- [ ] `run_metadata.json` generated
- [ ] Ruff checks pass
- [ ] pytest passes
- [ ] GitHub Actions CI passes

## 👨‍💻 Author

**Subhankar Biswas**  
M.Sc. Data Engineering  
Constructor University, Bremen, Germany

Focus areas:

```text
Data Engineering · Geospatial Analytics · Knowledge Graphs
Machine Learning · Data Pipelines · Network Analysis
Generative AI · Smart Cities
```

## 📄 License

This project is released under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

⭐ If this project is useful, consider starring the repository and using the architecture as a starting point for smart-city, geospatial analytics, knowledge-graph, or accessibility projects.
