from typing import Any


class Node:
    def __init__(self, item: Any):
        self.item = item
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.item)

    def __eq__(self, other):
        if not isinstance(other, Node):
            raise TypeError
        return self.item == other.item

    def __ne__(self, other):
        if not isinstance(other, Node):
            raise TypeError
        return self.item != other.item

    def __lt__(self, other):
        if not isinstance(other, Node):
            raise TypeError
        return self.item < other.item

    def __gt__(self, other):
        if not isinstance(other, Node):
            raise TypeError
        return self.item > other.item

    def __ge__(self, other):
        if not isinstance(other, Node):
            raise TypeError
        return self.item >= other.item

    def __le__(self, other):
        if not isinstance(other, Node):
            raise TypeError
        return self.item <= other.item