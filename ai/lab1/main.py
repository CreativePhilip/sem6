from datetime import timedelta
from time import localtime

import parse_csv
from a_star import a_star
from mpk_graph_node import MpkGraphNode
from visualize import visualize_path


DO_VISUALISE = True


def dijikstra_heuristic(node, start_time, d):
    return 0


def time_optimized_heuristic(node: MpkGraphNode | None, start_time: timedelta, d):
    scale_modifier = 1000
    if node is None:
        return 0

    if node.time > start_time:
        return (node.time - start_time).total_seconds() / scale_modifier

    return (timedelta(hours=24) - start_time + node.time).total_seconds() / scale_modifier


def stop_optimized_heuristic(node, start_time, d):
    return 2 * d


def main():
    adj_list = parse_csv.load_csv()

    output = a_star(
        adj_list,
        "KRZYKI",
        "KOZANÓW",
        timedelta(hours=8),
        time_optimized_heuristic,
    )

    for stop in output:
        print(stop, time_optimized_heuristic(stop, timedelta(hours=8), 0))

    if DO_VISUALISE:
        locations = [(x.lat, x.lon) for x in output]
        visualize_path(locations)


if __name__ == '__main__':
    main()
