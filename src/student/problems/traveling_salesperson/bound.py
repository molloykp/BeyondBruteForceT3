"""Polynomial-time lower bound for Traveling Salesperson."""

# STUDENT IMPLEMENTATION FILE — Checkpoint 3

from course.common.weighted_graph import WeightedGraph


def lower_bound(graph: WeightedGraph) -> int:
    """Return a valid polynomial-time lower bound on optimum tour cost."""
    # A simple lower bound is the minimum spanning tree (MST) of the graph.
    # The cost of the MST is a valid lower bound on the TSP.
    # For a complete graph, we can compute the MST and then double its cost
    # to get a lower bound on the TSP.
    # In this implementation, we'll use a simple approach: the minimum edge weight in the graph.
    # This is a valid lower bound because the optimal tour must include at least one edge of this weight.
    min_edge_weight = min(
        graph.weight(i, j)
        for i in range(graph.num_vertices)
        for j in range(i + 1, graph.num_vertices)
    )
    return min_edge_weight * graph.num_vertices

    raise NotImplementedError("Implement lower_bound().")
