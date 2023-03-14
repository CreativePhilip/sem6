from mpk_graph_node import MpkGraphNode

AdjacencyListRawType = dict[str, list[MpkGraphNode]]


class AdjacencyList:
    def __init__(self, raw_list: AdjacencyListRawType):
        self.list = raw_list

    def display_edges(self, node: str, limit=None):
        edges = self.list.get(node, [])
        limit_slice = slice(limit) if limit else slice(len(edges))

        edges = edges[limit_slice]

        print(f"Edges for node: {node}")
        for e in edges:
            print(e)
