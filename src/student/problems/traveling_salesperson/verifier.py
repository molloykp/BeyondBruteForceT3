"""Polynomial-time certificate verifier for Traveling Salesperson.

STUDENT IMPLEMENTATION FILE — Checkpoint 2

The decision problem asks whether ``graph`` contains a tour of total cost at
most ``k``.  ``tour`` is the proposed certificate.
"""

from course.common.weighted_graph import WeightedGraph


def is_valid_tour(graph: WeightedGraph, tour: list[int], k: int) -> bool:
    """Return True exactly when ``tour`` certifies a YES instance.

    Return True only when ``tour`` is a valid TSP tour of ``graph`` and the
    cost computed from the graph and tour is at most ``k``.  Do not trust a
    separately reported cost; compute the certificate's cost here.
    """
    if not tour or len(tour) != graph.num_vertices + 1:
        return False
    
    if tour[0] != tour[-1]:
        return False
    
    if not all(0 <= v < graph.num_vertices for v in tour):
        return False
    
    if len(set(tour[:-1])) != graph.num_vertices:
        return False
    # sum the costs of the edges in the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += graph.weight(tour[i], tour[i + 1])
    if total_cost > k:
        return False
    return True
