from algorithms.graphs.dijkstra import dijkstra

def test_dijkstra_path():
    graph = {
        "A": [("B", 1.0), ("C", 4.0)],
        "B": [("C", 2.0)],
        "C": []
    }
    dist, prev = dijkstra(graph, "A")
    assert dist["C"] == 3.0
    assert prev["C"] == "B"
