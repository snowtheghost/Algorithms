from typing import Any
from Graph import Graph
from DirectedGraph import DirectedGraph
from UndirectedGraph import UndirectedGraph
from Queue.Queue import Queue


def bfs(graph: Graph, source: Any) -> list:
    """
    Perform breadth-frist search on the given graph from the specified source vertex
    :param graph: the graph to perform bfs on
    :param source: the vertex to start from
    :return: a list of breadth-first traversal of format (vertex, distance, parent)
    """
    bfs_traversal = []
    vertices = graph.adjacency_list.keys()

    status = {}  # synonymous to colours, initialized at white (unvisited)
    distance = {}  # distance from source
    parent = {}  # parent of discovered vertex
    for vertex in vertices:
        status[vertex] = 0
        distance[vertex] = None  # indicates depth of disconnect
        parent[vertex] = None

    status[source] = 1  # initialize source at grey (visited but not explored completely)
    distance[source] = 0  # the distance from the source to itself is 0
    q = Queue()  # queue for vertices that need to be explored

    q.enqueue(source)
    while not q.is_empty():
        u = q.dequeue()
        for v in graph.adjacency_list[u]:
            if status[v] == 0:  # if vertex v is white
                status[v] = 1  # update v to grey
                distance[v] = distance[u] + 1
                parent[v] = u
                q.enqueue(v)
        status[u] = 2  # we have fully explored u, hence update u to black
        bfs_traversal.append((u, distance[u], parent[u]))

    return bfs_traversal


if __name__ == '__main__':
    graph = DirectedGraph()
    graph.add_vertices(["s", "a", "b", "c", "d", "e", "f"])
    graph.add_edges([("s", "a"), ("s", "f"), ("a", "b"), ("a", "e"), ("b", "c"),
                     ("b", "d"), ("c", "d"), ("c", "e"), ("e", "d"), ("e", "f")])
    print(graph)
    print(bfs(graph, "s"))
