from abc import abstractmethod, ABC
from typing import List, Any

from LinkedList.LinkedList import LinkedList


class Graph(ABC):
    def __init__(self):
        self.adjacency_list = {}

    def __str__(self) -> str:
        out_string = ""
        for item in self.adjacency_list:
            out_string += str(item) + ": "
            for connection in self.adjacency_list[item]:
                out_string += str(connection)
                out_string += ", "
            out_string = out_string[:-2]
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

    @abstractmethod
    def add_edge(self, item_u: Any, item_v: Any) -> None:
        raise NotImplementedError

    def add_edges(self, edges: List[tuple]) -> None:
        """
        Add all edges of the format (item_u, item_v)
        :param edges: all edges to be added
        :return:
        """
        for edge in edges:
            self.add_edge(edge[0], edge[1])

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

    @abstractmethod
    def delete_edge(self, item_u: Any, item_v: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def neighbourhood_query(self, item: Any) -> list:
        raise NotImplementedError

    def edge_query(self, item_u: Any, item_v: Any) -> bool:
        """
        :return: True if an edge exists between the two items, and False otherwise
        """
        try:
            if item_v in self.adjacency_list[item_u]:
                return True
            else:
                return False
        except KeyError:
            return False

    @abstractmethod
    def degree_query(self, item: Any) -> int:
        raise NotImplementedError
