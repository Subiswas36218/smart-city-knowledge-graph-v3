import pandas as pd
from src.rdf_kg import make_graph
from src.network_accessibility import threshold_coverage

def test_graph_constructs():
    assert len(make_graph()) == 0

def test_threshold_coverage():
    result = threshold_coverage(pd.DataFrame({"travel_time_min":[3,8,17,30]}))
    assert list(result.reached) == [1,2,2]
