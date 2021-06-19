from Node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.inorder_traversal())

    def inorder_traversal(self, node: Node = None, traversal: list = None):
        if not node:
            node = self.root

        if traversal is None:
            traversal = []

        if node:
            if node.left:
                self.inorder_traversal(node.left, traversal)

            traversal.append(node.value)

            if node.right:
                self.inorder_traversal(node.right, traversal)

        return traversal

    def insert(self, x: int) -> None:
        new_node = Node(x)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while True:
            if x < current.value:
                if not current.left:
                    current.left = new_node
                    return
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    return
                else:
                    current = current.right

    def delete(self, x: int) -> None:
        node = None
        current = self.root

        while current is not None:
            if x < current.value:
                current = current.left
            elif x > current.value:
                current = current.right
            else:
                node = current
                break

    # TODO: complete implementation






