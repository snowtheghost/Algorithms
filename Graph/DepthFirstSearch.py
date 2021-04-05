from typing import Any
from Graph import Graph
from DirectedGraph import DirectedGraph
from UndirectedGraph import UndirectedGraph


def dfs(graph: Graph) -> list:
    """
    Perform depth-first search on the given graph from the specified source vertex
    :param graph: the graph to perform dfs on
    :return: a list of depth-first traversal of format (vertex, discovery time, finish_time, parent)
    """
    dfs_traversal = []
    time = 0
    vertices = graph.adjacency_list.keys()

    status = {}  # synonymous to colours, initialized at white (unvisited)
    discovery_time = {}  # the time of vertex discovery
    finish_time = {}  # the time of complete vertex neighbourhood exploration
    parent = {}  # parent of discovered vertex
    for vertex in vertices:
        status[vertex] = 0
        discovery_time[vertex] = None
        finish_time[vertex] = None
        parent[vertex] = None

    for vertex in vertices:
        if status[vertex] == 0:
            time = dfs_visit(graph, vertex, time, status, discovery_time, finish_time, parent)

    for vertex in vertices:
        dfs_traversal.append((vertex, discovery_time[vertex], finish_time[vertex], parent[vertex]))
    return dfs_traversal


def dfs_visit(graph: Graph, u: Any, time: int, status: dict,
              discovery_time: dict, finish_time: dict, parent: dict) -> int:
    """
    Completely explores each vertex connected to the source vertex u, starting from lowest depth
    :param graph: the graph to perform dfs_visit on
    :param u: the vertex to recurse down
    :param time: the time called
    :return: the time after dfs_visit() completes on the source vertex
    """
    status[u] = 1  # update u to grey
    time += 1
    discovery_time[u] = time

    for v in graph.adjacency_list[u]:
        if status[v] == 0:
            parent[v] = u
            time = dfs_visit(graph, v, time, status, discovery_time, finish_time, parent)
    status[u] = 2
    time += 1
    finish_time[u] = time
    return time


if __name__ == '__main__':
    graph1 = DirectedGraph()
    graph1.add_vertices([1, 2, 3, 4, 5, 6, 7])
    graph1.add_edges([(1, 2), (1, 4), (1, 7), (2, 3), (2, 4),
                     (3, 1), (3, 4), (5, 4), (5, 6), (6, 3), (6, 5), (7, 1), (7, 4)])
    print(graph1)
    print(str(dfs(graph1)) + "\n")

    graph2 = DirectedGraph()
    graph2.add_vertices(["a", "b", "c", "d", "e", "f"])
    graph2.add_edges([("a", "b"), ("a", "d"), ("b", "e"), ("c", "f"), ("d", "b"), ("e", "d"), ("f", "d"), ("f", "f")])
    print(graph2)
    print(dfs(graph2))