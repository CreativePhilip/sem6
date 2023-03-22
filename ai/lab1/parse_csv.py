import csv
from pathlib import Path
from typing import Iterable, TypedDict

from adjacency_list import AdjacencyList
from mpk_graph_node import MpkGraphEdge


class ConnectionGraphType(TypedDict):
    line: str
    arrival_time: str
    departure_time: str

    end_stop: str
    end_stop_lat: str
    end_stop_lon: str

    start_stop: str
    start_stop_lat: str
    start_stop_lon: str


def load_csv(filename: str = "connection_graph.csv") -> AdjacencyList:
    file_path = Path(__file__).parent / f"data/{filename}"

    reader: Iterable[ConnectionGraphType] = csv.DictReader(open(file_path))
    it = map(parse_into_model, reader)
    return parse_into_adjacency_list(it)


def parse_into_model(instance: ConnectionGraphType) -> MpkGraphEdge:
    return MpkGraphEdge(**instance)


def parse_into_adjacency_list(it: Iterable[MpkGraphEdge]) -> AdjacencyList:
    adj_list: AdjacencyList = {}

    for node in it:
        adj_list.setdefault(node.start_stop, []).append(node)

    return AdjacencyList(adj_list)
