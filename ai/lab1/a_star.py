from collections import defaultdict
from datetime import timedelta
from typing import Callable

from adjacency_list import AdjacencyList
from mpk_graph_node import MpkGraphNode

HeuristicFunType = Callable[[str, timedelta, int], float | int]
POSITIVE_INFINITY = float("inf")


def a_star(
        adj_list: AdjacencyList,
        start_node_name: str,
        end_node_name: str,
        start_time: timedelta,
        h: HeuristicFunType,
):
    start_node = adj_list.get_node_by_name_with_min_h(start_node_name, lambda node: h(node, start_time, 0))
    end_node = adj_list.get_node_by_name(end_node_name)

    open_list: set[MpkGraphNode] = {start_node}
    end_list = set()

    # g represents current distances from the start node
    g = defaultdict(lambda: POSITIVE_INFINITY)
    g[start_node] = 0

    parents = {start_node: start_node}

    while open_list:
        current_node: MpkGraphNode | None = None

        for open_value in open_list:
            if current_node is None:
                current_node = open_value

            current_weight = g[current_node] + h(current_node, current_node.time, 0)
            open_weight = g[open_value] + h(open_value, current_node.time, 0)

            if open_weight < current_weight:
                current_node = open_value

        if current_node is None:
            return None

        if current_node.name == end_node.name:
            path = []

            while parents[current_node] != current_node:
                path.append(current_node)
                current_node = parents[current_node]

            path.append(start_node)
            path.reverse()

            return path

        for test_edge in adj_list.neighbours(current_node):
            test_edge_end_node = test_edge.end_as_node()
            test_distance = test_edge.distance()

            temp_new_g_value = g[current_node] + test_distance

            if test_edge_end_node not in open_list and test_edge_end_node not in end_list:
                open_list.add(test_edge_end_node)
                parents[test_edge_end_node] = current_node
                g[test_edge_end_node] = temp_new_g_value
            else:
                if g[test_edge_end_node] > temp_new_g_value:
                    g[test_edge_end_node] = temp_new_g_value
                    parents[test_edge_end_node] = current_node

                    if test_edge_end_node in end_list:
                        end_list.remove(test_edge_end_node)
                    if test_edge_end_node in open_list:
                        open_list.remove(test_edge_end_node)

        open_list.remove(current_node)
        end_list.add(current_node)

    return None





def get_current_depth(start, current, tree):
    return 0
