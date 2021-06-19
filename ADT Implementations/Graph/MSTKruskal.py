from DisjointSet.DisjointSet import DisjointSet
from WeightedGraph import WeightedGraph
from random import randrange


def MSTKruskal(graph: WeightedGraph):
    mst = WeightedGraph()
    djs = DisjointSet()
    edges = sort_edges(graph.edges, graph.weights)
    vertices = graph.adjacency_list.keys()

    for vertex in vertices:
        djs.make_set(vertex)
        mst.add_vertex(vertex)

    for edge in edges:
        if djs.find_set(edge[0]) != djs.find_set(edge[1]):
            print(edge)
            djs.union(edge[0], edge[1])
            mst.add_weighted_edge(edge[0], edge[1], graph.weights[edge])

    return mst


def sort_edges(edges: list, weights: dict) -> list:
    """
    :param weights: a dictionary of edges to weights
    :param edges: a list of edges to be sorted
    :return: a new list of sorted edges (using randomized quicksort)
    """
    if len(edges) <= 1:  # Do nothing if the list is not sortable
        return edges[:]
    else:
        pivot_index = randrange(0, len(edges))
        pivot = edges[pivot_index]  # Choose the pivot to be the first item i
        split = partition_edges(edges[:pivot_index] + edges[pivot_index+1:], weights, pivot)
        left = split[0]
        right = split[1]
        left = sort_edges(left, weights)
        right = sort_edges(right, weights)
        return left + [pivot] + right


def partition_edges(edges: list, weights: dict, pivot: int) -> list:
    """
    :param weights: a dictionary of edges to weights
    :param edges: a list of sortable edges
    :param pivot: the item chosen as the pivot
    :return: a list of two lists, where the left list contains all edges leq to the pivot and the right list contains
    the remaining edges
    """
    left = []
    right = []
    for edge in edges:
        if weights[edge] <= weights[pivot]:
            left.append(edge)
        else:
            right.append(edge)
    return [left, right]


if __name__ == "__main__":
    graph = WeightedGraph()
    graph.add_vertices(["A", "B", "C", "D", "E", "F", "G", "H"])
    graph.add_weighted_edges([("A", "B", 4), ("A", "D", 3), ("A", "E", 3), ("B", "C", 10), ("B", "D", 1), ("B", "E", 2),
                              ("C", "E", 8), ("C", "F", 8), ("C", "G", 12), ("D", "E", 1), ("E", "F", 9), ("G", "H", 2)])
    print(graph)
    print(MSTKruskal(graph))

    graph = WeightedGraph()
    graph.add_vertices(["A", "B", "C", "D", "E", "F", "G"])
    graph.add_weighted_edges([("A", "B", 5), ("A", "C", 4), ("B", "C", 6), ("B", "D", 2), ("B", "E", 7), ("B", "F", 10),
                              ("C", "D", 10), ("C", "E", 10), ("C", "F", 10), ("D", "E", 3), ("D", "F", 8),
                              ("E", "F", 1), ("E", "G", 10), ("F", "G", 9)])
    print(graph)
    print(MSTKruskal(graph))
