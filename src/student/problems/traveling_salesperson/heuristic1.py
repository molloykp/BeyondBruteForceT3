"""Traveling Salesperson — first heuristic solver."""

# STUDENT IMPLEMENTATION FILE — Checkpoint 3
# Keep the required solve() signature and return structure.

from argparse import Namespace
from time import perf_counter

from course.common.weighted_graph import WeightedGraph
import sys
import random


def solve(instance: WeightedGraph, args: Namespace) -> tuple[dict, dict]:
    """Return a solution dictionary and a statistics dictionary."""
    start_time = perf_counter()

    # TODO: Implement the first heuristic algorithm.
    tour: list[int] = []
    cost = sys.maxsize
    for i in range(50):
        this_tour = list(range(1, instance.num_vertices))

        random.shuffle(this_tour)
        this_tour = [0] + this_tour + [0]
        this_cost = sum(instance.weight(this_tour[i], this_tour[i + 1]) 
                        for i in range(instance.num_vertices))
        if this_cost < cost:
            cost = this_cost
            tour = this_tour
    solution = {
        "cost": cost,
        "tour": tour,
    }

    statistics = {
        "time": perf_counter() - start_time,
    }

    return solution, statistics
