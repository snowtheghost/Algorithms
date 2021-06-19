# TODO: Deletion

from typing import Optional, Any
from Node import Node


class AVL:
    def __init__(self):
        self.root = None

    def __str__(self):
        """
        :return: preorder traversal of the tree
        """
        return str(self.preorder())

    def get_root(self):
        return self.root

    def insert(self, item: Any, current: Optional[Node]) -> None:
        """
        AVL insertion with rebalancing
        :param item: the item to be inserted
        :param current: the node at the root of the subtree to insert into
        """
        # BST insertion
        if not current:
            current = self.root
            if self.root is None:
                self.root = Node(item)
                return
        if item < current.item:
            if current.left:
                self.insert(item, current.left)
            else:
                current.left = Node(item)
        else:  # node >= current
            if current.right:
                self.insert(item, current.right)
            else:
                current.right = Node(item)

        # Update height and rebalance
        self.update_height(current)
        self.rebalance(current)

    def rotate_left(self, target: Node, parent: Optional[Node] = None) -> None:
        """
        Perform a left rotation on the tree rooted at the current node
        Precondition: target node has a right child
        :param parent: the parent of the target node
        :param target: the root of the tree to perform the rotation on
        """
        if parent is not None:
            if parent.left == target:
                parent.left = target.right
                root = parent.left
            else:  # parent.right == current
                parent.right = target.right
                root = parent.right
        else:
            self.root = target.right
            root = self.root
        target.right = root.left
        root.left = target

        self.update_height(root)
        self.update_height(target)

    def rotate_right(self, target: Node, parent: Optional[Node] = None) -> None:
        """
        Perform a left rotation on the tree rooted at the current node
        Precondition: target node has a left child
        :param parent: the parent of the target node
        :param target: the root of the tree to perform the rotation on
        """
        if parent is not None:
            if parent.left == target:
                parent.left = target.left
                root = parent.left
            else:  # parent.right == current
                parent.right = target.left
                root = parent.right
        else:
            self.root = target.left
            root = self.root
        target.left = root.right
        root.right = target

        self.update_height(root)
        self.update_height(target)

    def rebalance(self, current) -> None:
        """
        Check and rebalance each child of the current node, and the current node when current == self.root
        :param current: the current node being visited
        """
        if current.left:
            if self.get_bf(current.left) > 1:
                if self.get_bf(current.left.right) < 0:
                    self.rotate_right(current.left.right, current.left)
                self.rotate_left(current.left)
            elif self.get_bf(current.left) < -1:
                if self.get_bf(current.left.left) > 0:
                    self.rotate_right(current.left.left, current.left)
                self.rotate_right(current.left)
            else:
                pass
        if current.right:
            if self.get_bf(current.right) > 1:
                if self.get_bf(current.right.right) < 0:
                    self.rotate_right(current.right.right, current.right)
                self.rotate_left(current.right)
            elif self.get_bf(current.right) < -1:
                if self.get_bf(current.right.left) > 0:
                    self.rotate_right(current.right.left, current.right)
                self.rotate_right(current.right)
            else:
                pass

    def preorder(self, current: Optional[Node] = None) -> list:
        """
        :return: preorder traversal of the tree in list form
        """
        preorder = []
        if not current:
            current = self.root
        preorder.append(current.item)
        if current.left:
            preorder.extend(self.preorder(current.left))
        if current.right:
            preorder.extend(self.preorder(current.right))
        return preorder

    def get_height(self, node: Optional[Node]) -> int:
        """
        Get the height of the node
        :param node: the node of which to check
        :return: the height of the node, or -1 if None
        """
        if node:
            return node.height
        else:
            return -1

    def update_height(self, node: Optional[Node]) -> None:
        """
        :param node: the node of which to update
        """
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_bf(self, node: Node) -> int:
        return self.get_height(node.right) - self.get_height(node.left)

    def bst_insert(self, item: Any, current: Optional[Node] = None) -> None:
        """
        Binary search tree insert with no BF checking or rebalancing
        :param item: the item to be inserted
        :param current: the node at the root of the subtree to insert into
        """
        if not current:
            current = self.root
            if self.root is None:
                self.root = Node(item)
                return
        if item < current.item:
            if current.left:
                self.bst_insert(item, current.left)
            else:
                current.left = Node(item)
        else:  # node >= current
            if current.right:
                self.bst_insert(item, current.right)
            else:
                current.right = Node(item)
        self.update_height(current)
