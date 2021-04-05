from typing import Any, Union

from UndirectedGraph import UndirectedGraph


class WeightedGraph(UndirectedGraph):
    def __init__(self):
        super().__init__()
        self.weights = {}

    def __str__(self) -> str:
        out_string = ""
        for item in self.adjacency_list:
            out_string += str(item) + ": "
            for connection in self.adjacency_list[item]:
                weighted_connection = (connection, self.weights[(item, connection)])
                out_string += str(weighted_connection)
                out_string += ", "
            out_string = out_string[:-2]
            out_string += "\n"
        return out_string

    def add_weighted_edge(self, item_u: Any, item_v: Any, weight: Union[int, float]) -> None:
        """
        Add an edge from u to v
        Preconditions: the item and all items in connections exist in the graph,
        and the connections have not already been made
        """
        super().add_edge(item_u, item_v)
        self.weights[(item_u, item_v)] = weight
        self.weights[(item_v, item_u)] = weight

    def add_weighted_edges(self, edges: list) -> None:
        """
        :param edges: a tuple of format (u, v, weight)
        """
        for edge in edges:
            self.add_weighted_edge(edge[0], edge[1], edge[2])

    def add_edge(self, item_u: Any, item_v: Any) -> None:
        """
        Add an edge of weight 0
        """
        self.add_weighted_edge(item_u, item_v, 0)


if __name__ == "__main__":
    graph = WeightedGraph()
    graph.add_vertices(["p", "q", "r", "s", "t"])
    graph.add_weighted_edges([("t", "s", 5), ("t", "q", 1), ("t", "r", 4), ("q", "r", 3), ("s", "p", 2), ("r", "p", 2.5)])
    print(graph)
