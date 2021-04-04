from typing import Any

from LinkedList.LinkedList import LinkedList


class UndirectedGraph:
    adjacency_list = {}

    def __str__(self) -> str:
        out_string = ""
        for item in self.adjacency_list:
            out_string += item
            for connection in self.adjacency_list[item]:
                out_string += " -> "
                out_string += connection
            out_string += "\n"
        return out_string

    def add_vertex(self, item: any) -> None:
        """
        Add a new vertex with no edges
        Precondition: the item does not exist in the graph
        :param item: the value of the vertex to insert
        """
        self.adjacency_list[item] = LinkedList()

    def add_vertices(self, items: list) -> None:
        """
        Performs the same operation as add_vertex() over a list of items
        :param items: the values of the vertices to insert
        """
        for item in items:
            self.add_vertex(item)

    def add_edges(self, item: Any, connections: list) -> None:
        """
        Connects the item to each item in connections
        Preconditions: the item and all items in connections exist in the graph,
        and the connections have not already been made
        :param item: the main item to be connected to
        :param connections: all items that the main item should be connected to
        """
        self.adjacency_list[item].insert_all(connections)
        for connection in connections:
            self.adjacency_list[connection].insert(item)

    def delete_vertex(self, item: Any) -> None:
        """
        Precondition: item is in the graph
        Deletes a vertex and any edges associated with the vertex
        :param item: the identifier of the vertex
        """
        self.adjacency_list.pop(item)
        for key in self.adjacency_list:
            if item in self.adjacency_list[key]:
                self.adjacency_list[key].delete(item)

    def delete_edge(self, item_u: Any, item_v: Any) -> None:
        """
        Precondition: the edge between the two items exists
        """
        self.adjacency_list[item_u].delete(item_v)
        self.adjacency_list[item_v].delete(item_u)

    def edge_query(self, item_u: Any, item_v: Any) -> bool:
        """
        :return: True if an edge exists between the two items, and False otherwise
        """
        try:
            if item_v in self.adjacency_list[item_u]:  # Assumes correctness of all previous operations
                return True
            else:
                return False
        except KeyError:
            return False

    def neighbourhood_query(self, item: Any) -> list:
        """
        Precondition: item must exist in the graph
        :param item: the vertex of which the neighbourhood is queried
        :return: a list of vertices that share an edge with the vertex
        """
        neighbours = []
        for item in self.adjacency_list[item]:
            neighbours.append(item)
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
    graph.add_edges("a", ["b", "c", "d"])
    graph.add_edges("b", ["d"])

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

    print(str(graph.degree_query("c")) + "\n")
