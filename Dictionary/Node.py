from typing import Any, Optional


class Node:
    def __init__(self, key: Any, value: Any):
        """
        :param key: the key of the Node
        :param value: the value of the Node
        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def get_height(self) -> int:
        """
        :return: the height of the subtree rooted at the self
        """
        return self.height

    def update_height(self) -> None:
        """
        Updates the height of the subtree rooted at the self
        """
        self.height = 1 + max(get_height(self.left), get_height(self.right))

    def get_bf(self) -> int:
        """
        :return: the balance factor of the subtree rooted at the self
        """
        return get_height(self.right) - get_height(self.left)


def get_height(node: Optional[Node]):
    """
    :param node: the (potential) node to find the height for
    :return: the height of the node, or -1 if the node does not exist
    """
    if node is None:
        return -1
    else:
        return node.get_height()
