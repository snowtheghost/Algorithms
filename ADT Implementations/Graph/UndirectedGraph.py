from typing import Any
from Graph import Graph
from LinkedList.LinkedList import LinkedList


class UndirectedGraph(Graph):
    def add_edge(self, item_u: Any, item_v: Any) -> None:
        """
        Add an edge from u to v
        Preconditions: the item and all items in connections exist in the graph,
        and the connections have not already been made
        """
        self.adjacency_list[item_u].insert(item_v)
        self.adjacency_list[item_v].insert(item_u)

    def delete_edge(self, item_u: Any, item_v: Any) -> None:
        """
        Precondition: the edge between the two items exists
        """
        self.adjacency_list[item_u].delete(item_v)
        self.adjacency_list[item_v].delete(item_u)

    def neighbourhood_query(self, item: Any) -> list:
        """
        Precondition: item must exist in the graph
        :param item: the vertex of which the neighbourhood is queried
        :return: a list of vertices that share an edge with the vertex
        """
        neighbours = []
        for neighbour in self.adjacency_list[item]:
            neighbours.append(neighbour)
        return neighbours

    def degree_query(self, item: Any) -> int:
        """
        Precondition: item must exist in the graph
        :param item: the vertex of which the degree is queried
        :return: the number of incident edges on the queried vertex
        """
        return len(self.adjacency_list[item])


if __name__ == '__main__':
    graph = UndirectedGraph()
    graph.add_vertices(["a", "b", "c", "d"])
    graph.add_edges([("a", "b"), ("a", "c"), ("a", "d"), ("b", "d")])

    print(graph)

    print(str(graph.neighbourhood_query("b")) + "\n")

    print(str(graph.degree_query("a")) + "\n")

    graph.delete_vertex("b")
    print(graph)

    graph.delete_edge("c", "a")
    print(graph)

    print(graph.edge_query("c", "d"))
    print(graph.edge_query("d", "a"))
    print(str(graph.edge_query("b", "c")) + "\n")

    print(str(graph.degree_query("d")) + "\n")
