from typing import Any, List
from LinkedList.LinkedList import LinkedList
from Graph import Graph


class DirectedGraph(Graph):
    def add_edge(self, item_u: Any, item_v: Any) -> None:
        """
        Add an edge from u to v
        Preconditions: the item and all items in connections exist in the graph,
        and the connections have not already been made
        """
        self.adjacency_list[item_u].insert(item_v)

    def delete_edge(self, item_u: Any, item_v: Any) -> None:
        """
        Precondition: the edge (u, v) exists
        """
        self.adjacency_list[item_u].delete(item_v)

    def out_neighbourhood_query(self, item: Any) -> list:
        """
        Precondition: item must exist in the graph
        :param item: the vertex of which the neighbourhood is queried
        :return: a list of vertices that share an out edge with the vertex
        """
        out_neighbours = []
        for vertex in self.adjacency_list[item]:
            out_neighbours.append(vertex)
        return out_neighbours

    def in_neighbourhood_query(self, item: Any) -> list:
        """
        Precondition: item must exist in the graph
        :param item: the vertex of which the neighbourhood is queried
        :return: a list of vertices that share an in edge with the vertex
        """
        in_neighbours = []
        for vertex in self.adjacency_list:
            if item in self.adjacency_list[vertex]:
                in_neighbours.append(vertex)
        return in_neighbours

    def neighbourhood_query(self, item: Any) -> list:
        """
        Precondition: item must exist in the graph
        :param item: the vertex of which the neighbourhood is queried
        :return: a list of vertices that share an edge with the vertex
        """
        neighbours = self.out_neighbourhood_query(item) + self.in_neighbourhood_query(item)
        if item in neighbours:
            neighbours.remove(item)  # remove duplicate in and out neighbour of self
        return self.out_neighbourhood_query(item) + self.in_neighbourhood_query(item)

    def out_degree_query(self, item: Any) -> int:
        """
        Precondition: item must exist in the graph
        :param item: the vertex of which the out degree is queried
        :return: the number of out edges on the queried vertex
        """
        return len(self.adjacency_list[item])

    def in_degree_query(self, item: Any) -> int:
        """
        Precondition: item must exist in the graph
        :param item: the vertex of which the in degree is queried
        :return: the number of in edges on the queried vertex
        """
        in_degree = 0
        for vertex in self.adjacency_list:
            if item in self.adjacency_list[vertex]:
                in_degree += 1
        return in_degree

    def degree_query(self, item: Any) -> int:
        """
        Precondition: item must exist in the graph
        :param item: the vertex of which the degree is queried
        :return: the number of incident edges on the queried vertex
        """
        return self.out_degree_query(item) + self.in_degree_query(item)


if __name__ == '__main__':
    graph = DirectedGraph()
    graph.add_vertices(["a", "b", "c", "d", "e", "f"])
    graph.add_edges([("a", "b"), ("a", "d"), ("b", "e"), ("c", "f"), ("d", "b"), ("e", "d"), ("f", "d")])

    print(graph)

    print(str(graph.neighbourhood_query("b")) + "\n")

    print(str(graph.degree_query("a")) + "\n")

    graph.delete_vertex("b")
    print(graph)

    graph.delete_edge("f", "d")
    print(graph)

    print(graph.edge_query("c", "f"))
    print(graph.edge_query("d", "a"))
    print(str(graph.edge_query("b", "e")) + "\n")

    print(str(graph.degree_query("d")) + "\n")
