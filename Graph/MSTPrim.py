from typing import Any

from WeightedGraph import WeightedGraph
from PriorityQueue.PriorityQueue import MinPriorityQueue


def MSTPrim(graph: WeightedGraph, root: Any) -> WeightedGraph:
    """
    Prim's algorithm to creating an MST from a weighted graph
    :param graph: a weighted graph of which we extract an MST from
    :param root: the first node to consider
    :return: an MST of the graph
    """
    vertices = graph.adjacency_list.keys()
    mst = WeightedGraph()
    priority = {}
    parent = {}
    for vertex in vertices:
        priority[vertex] = max(graph.weights.values())  # Acts as infinity
        parent[vertex] = None
    priority[root] = 0

    q = MinPriorityQueue()
    for vertex in vertices:
        q.insert(vertex, priority[vertex])

    while not q.is_empty():
        node = q.extract_min()
        u = node.value
        u_weight = node.priority
        mst.add_vertex(u)
        if parent[u] is not None:
            mst.add_weighted_edge(u, parent[u], u_weight)

        for v in graph.adjacency_list[u]:
            if v in q and graph.weights[(u, v)] < priority[v]:
                priority[v] = graph.weights[(u, v)]
                q.update_priority(v, priority[v])
                parent[v] = u
    return mst


if __name__ == "__main__":
    graph = WeightedGraph()
    graph.add_vertices(["A", "B", "C", "D", "E", "F"])
    graph.add_weighted_edges([("A", "B", 4), ("A", "D", 3), ("A", "E", 3), ("B", "C", 10), ("B", "D", 1),
                              ("B", "E", 2), ("C", "E", 8), ("C", "F", 8), ("D", "E", 1), ("E", "F", 9)])
    print(graph)
    print(MSTPrim(graph, "c"))

