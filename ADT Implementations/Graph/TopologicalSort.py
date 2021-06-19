from typing import Any

from Graph import Graph
from UndirectedGraph import UndirectedGraph
from DirectedGraph import DirectedGraph
from DepthFirstSearch import dfs
from LinkedList.LinkedList import LinkedList


def topological_sort(graph: Graph) -> LinkedList:
    """
    :param graph: the graph to sort
    :return: LinkedList such that if the graph contains edge (u, v), then u appears before v in the list
    """
    topological_list = LinkedList()

    time = 0
    vertices = graph.adjacency_list.keys()

    status = {}  # synonymous to colours, initialized at white (unvisited)
    for vertex in vertices:
        status[vertex] = 0

    for vertex in vertices:
        if status[vertex] == 0:
            dfs_visit(graph, vertex, time, status, topological_list)

    return topological_list


def dfs_visit(graph: Graph, u: Any, time: int, status: dict, topological_list: LinkedList) -> None:
    """
    Completely explores each vertex connected to the source vertex u, starting from lowest depth
    :param graph: the graph to perform dfs_visit on
    :param u: the vertex to recurse down
    :param time: the time called
    :return: the time after dfs_visit() completes on the source vertex
    """
    status[u] = 1  # update u to grey
    time += 1

    for v in graph.adjacency_list[u]:
        if status[v] == 0:
            dfs_visit(graph, v, time, status, topological_list)
    status[u] = 2
    time += 1
    topological_list.insert_first(u)


if __name__ == '__main__':
    graph = DirectedGraph()
    graph.add_vertices(["a", "b", "c", "d", "e", "f"])
    graph.add_edges([("a", "b"), ("a", "d"), ("b", "e"), ("c", "f"), ("d", "b"), ("f", "d")])
    print(graph)
    print(topological_sort(graph))