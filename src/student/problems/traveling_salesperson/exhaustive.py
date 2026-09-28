"""Traveling Salesperson — baseline exhaustive exact solver."""

# STUDENT IMPLEMENTATION FILE — Checkpoint 2
# Keep the required solve() signature and return structure.

from argparse import Namespace
from time import perf_counter

from course.common.weighted_graph import WeightedGraph
from .verifier import is_valid_tour
import sys
from itertools import permutations


def solve(instance: WeightedGraph, args: Namespace) -> tuple[dict, dict]:
    """Return a solution dictionary and a statistics dictionary."""
    start_time = perf_counter()

    # TODO: Implement the baseline exhaustive exact algorithm.
    # Once a candidate tour cost c is known, it can be checked with is_valid_tour(instance, tour, c).
    tour: list[int] = []
    cost = sys.maxsize
    for perm in permutations(range(1,instance.num_vertices)):
        this_cost = 0
        this_tour = [0] + list(perm) + [0]
        this_tour_cost = [sum(instance.weight(this_tour[i],this_tour[i + 1]) for i in range(instance.num_vertices))][0]
        if this_tour_cost < cost:
            cost = this_tour_cost
            tour = this_tour
    solution = {
        "cost": cost,
        "tour": tour,
    }

    statistics = {
        "time": perf_counter() - start_time,
    }

    return solution, statistics
