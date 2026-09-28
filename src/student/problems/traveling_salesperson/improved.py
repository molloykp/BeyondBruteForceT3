"""Traveling Salesperson — improved exact solver."""

# STUDENT IMPLEMENTATION FILE — Checkpoint 3
# Keep the required solve() signature and return structure.

from argparse import Namespace
from time import perf_counter
import sys

from course.common.weighted_graph import WeightedGraph


def solve(instance: WeightedGraph, args: Namespace) -> tuple[dict, dict]:
    """Return a solution dictionary and a statistics dictionary."""
    start_time = perf_counter()

    # TODO: Implement the improved exact algorithm.
    tour: list[int] = []
    cost = sys.maxsize
    # use recursive backtracking
    def backtrack(current_tour, current_cost):
        nonlocal cost, tour

        if len(current_tour) == instance.num_vertices:
            # Complete the tour by returning to the starting city
            final_cost = current_cost + instance.weight(current_tour[-1], 0)
            if final_cost < cost:
                cost = final_cost
                tour = current_tour + [0]
        else:
            for i in range(1, instance.num_vertices):
                if i not in current_tour:
                    new_cost = current_cost + instance.weight(current_tour[-1], i)
                    if new_cost < cost:  # Pruning
                        backtrack(current_tour + [i], new_cost)

    backtrack([0], 0)

    solution = {
        "cost": cost,
        "tour": tour,
    }

    statistics = {
        "time": perf_counter() - start_time,
    }

    return solution, statistics
