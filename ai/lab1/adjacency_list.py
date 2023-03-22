from datetime import timedelta

from mpk_graph_node import MpkGraphEdge, MpkGraphNode

AdjacencyListRawType = dict[str, list[MpkGraphEdge]]


class AdjacencyList:
    def __init__(self, raw_list: AdjacencyListRawType):
        self.list = raw_list

    def neighbours(self, node: MpkGraphNode):
        return self.list.get(node.name, [])

    def get_node_by_name(self, name: str) -> MpkGraphNode:
        for k, v in self.list.items():
            if k == name:
                edge = v[0]
                return MpkGraphNode(
                    name=name,
                    time=edge.arrival_time,
                    lat=edge.start_stop_lat,
                    lon=edge.start_stop_lon,
                )

        raise ValueError("tifuck")

    def get_node_by_name_with_min_h(self, name: str, h) -> MpkGraphNode:
        for k, v in self.list.items():
            if k == name:
                edges = [(edge, h(edge.start_as_node())) for edge in v]
                edge, h_val = min(edges, key=lambda x: x[1])
                return MpkGraphNode(
                    name=name,
                    time=edge.arrival_time,
                    lat=edge.start_stop_lat,
                    lon=edge.start_stop_lon,
                )

        raise ValueError("tifuck")

    def get_node_location(self, name: str) -> tuple[float, float]:
        for k, v in self.list.items():
            if k == name:
                return v[0].start_stop_lat, v[0].start_stop_lon

        raise ValueError("tifuck")

    def display_edges(self, node: str, limit=None):
        edges = self.list.get(node, [])
        limit_slice = slice(limit) if limit else slice(len(edges))

        edges = edges[limit_slice]

        print(f"Edges for node: {node}")
        for e in edges:
            print(e)
