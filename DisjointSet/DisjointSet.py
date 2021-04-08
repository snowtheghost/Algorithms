from typing import Any

from LinkedList.LinkedList import Node, LinkedList


class Set:
    def __init__(self, initial_node: Node):
        self.rank = 0
        self.items = LinkedList()
        self.items.insert_node(initial_node)


class DisjointSet:
    def __init__(self):
        self.sets = {}  # key: representative node, value: Set
        self.nodes = {}

    def __str__(self):
        s = ""
        for item in self.nodes.keys():
            s += f"{item} -> {djs.nodes[item].next} \n"
        return s

    def make_set(self, representative: Any) -> Node:
        """
        Create a set containing only the representative given
        :param representative: the initial element of the set to be created
        """
        initial_node = Node(representative)
        self.sets[initial_node] = Set(initial_node)
        self.nodes[representative] = initial_node
        return initial_node

    def find_set(self, item: Any) -> Any:
        """
        :param item: the item of which its set is queried
        :return: the representative node of the set that the node is a member of
        """
        nodes = []
        node = self.nodes[item]
        while node.next is not None:
            nodes.append(node)
            node = node.next
        parent = node
        for node in nodes:
            node.next = parent
        return parent.item

    def union(self, x: Any, y: Any) -> Any:
        """
        :param x: an item of a set A
        :param y: an item of a set B
        :return: the representative of the new set AUB
        """
        x = self.nodes[self.find_set(x)]
        y = self.nodes[self.find_set(y)]

        if x == y:
            return x.item

        if self.sets[x].rank == self.sets[y].rank:
            self.sets[x].rank += 1
        elif self.sets[x].rank < self.sets[y].rank:
            x, y = y, x
        y.next = x
        self.sets.pop(y)

        return x.item


if __name__ == "__main__":
    djs = DisjointSet()
    items = ["a", "b", "c", "d", "e", "f", "g"]
    for item in items:
        djs.make_set(item)

    djs.union("e", "f")
    print(djs)

    djs.union("b", "d")
    print(djs)

    djs.union("d", "e")
    print(djs)

    djs.union("a", "c")
    print(djs)

    djs.union("a", "b")
    print(djs)

    djs.union("b", "c")
    print(djs)

    djs.union("b", "e")
    print(djs)

    djs.union("d", "f")
    print(djs)

    djs.union("f", "g")
    print(djs)
