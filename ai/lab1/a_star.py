from collections import defaultdict
from numbers import Number
from typing import Callable

from adjacency_list import AdjacencyList

HeuristicFunType = Callable[[str, AdjacencyList], Number]
POSITIVE_INFINITY = float("inf")


def a_star(
        adj_list: AdjacencyList,
        start_node: str,
        end_node: str,
        h: HeuristicFunType,
):
    open_list = {[start_node]}
    end_list = {[]}

    # g represents current distances from the start node
    g = defaultdict(lambda: POSITIVE_INFINITY, **{start_node: 0})

    parents = {start_node: start_node}

    while open_list:
        current_node: str | None = None

        for open_value in open_list:
            if current_node is None or g[open_value] + h(open_value) < g[current_node] + h(current_node):
                current_node = open_value

        if current_node is None:
            return None
