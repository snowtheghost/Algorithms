from typing import List, Union, Optional, Any
from Node import Node


class AVL:
    root = None

    def __str__(self) -> str:
        """
        :return: array depth inorder representation of the tree
        """
        return str(self.human_key(self.root))

    def __contains__(self, key: Any) -> bool:
        """
        :param key: the key to be found
        :return: True if the key is in the tree, and False otherwise
        """
        node = self.root

        while node is not None:
            if key < node.key:
                node = self.root.left
            elif key > node.key:
                node = self.root.right
            else:  # key == node.key
                return True
            return False

    def insert(self, node: Optional[Node], key: Any, value: Any) -> None:
        """
        :param node: the root of the subtree requested for insertion
        :param key: the key of the Node to be inserted
        :param value: the value of the Node to be inserted
        """
        new_node = Node(key, value)
        if node is None:
            self.root = new_node
            return

        if key < node.key:
            if node.left is None:
                node.left = new_node
            else:
                self.insert(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = new_node
            else:
                self.insert(node.right, key, value)
        else:  # key == node.key
            pass  # TODO: Possible extension

        node.update_height()
        rebalance(node)

    def search(self, node: Node, key: Any) -> Optional[Any]:
        """
        :param node: the root of the subtree requested for searching
        :param key: the key to be found
        :return: the value of the key that is found, or None if it is not found
        """
        if node.left is not None and key < node.key:
            return self.search(node.left, key)
        elif node.right is not None and key > node.key:
            return self.search(node.right, key)
        elif key == node.key:
            return node.value
        else:
            return None

    def delete(self, node: Optional[Node], key: Any) -> None:
        """
        Precondition: key in self
        :param node: the root of the subtree containing the node to be deleted
        :param key: the key of the node to be deleted
        """
        if node is None:
            if self.root.key == key:
                self.root = self.replace(None)
                if self.root is not None:
                    self.root.update_height()
                return
            else:
                node = self.root

        if key < node.key:  # key is in the left subtree of the node
            # check if the root of the left subtree is to be deleted
            if key == node.left.key:
                node.left = self.replace(node.left)
            else:  # root of left subtree is not to be deleted
                self.delete(node.left, key)
        else:  # key > node.key as we check for equality in the previous run
            # check if the root of the right subtree is to be deleted
            if key == node.right.key:
                node.right = self.replace(node.right)
            else:  # root of right subtree is not to be deleted
                self.delete(node.right, key)

        # update the height of the node and rebalance if necessary
        node.update_height()
        rebalance(node)

    def replace(self, node: Optional[Node]) -> Optional[Node]:
        """
        Deletes the node and returns the replacement with all necessary
        branches intact and updated
        :param node: the node to be deleted
        :return: the replacement for the deleted node, or None if none needed
        """
        if node.right is not None:  # a successor exists
            replacement = self.take_successor(node)
            replacement.left = node.left
        elif node.left is not None:  # no successor, but a predecessor exists
            replacement = self.take_predecessor(node)
            replacement.right = node.right  # should be None
        else:  # no successor or predecessor => node is a leaf
            replacement = None

        # update the height of the replacement and rebalance
        replacement.update_height()
        rebalance(replacement)
        return replacement

    def take_successor(self, node: Node) -> Node:
        """
        Removes the successor of node and updates/rebalance accordingly
        :param node: the root of the requested successor
        :return: the successor of the node
        """
        if node.right.left is None:
            successor = node.right
        else:  # the right subtree has a left subtree
            successor = self.take_smallest(node.right)

        successor.update_height()
        rebalance(successor)
        return successor

    def take_smallest(self, node: Node) -> Node:
        """
        Removes the smallest node of the subtree rooted at node and
        update/rebalance accordingly
        :param node: the root of the subtree to be operated on
        :return: the smallest node of the subtree rooted at node
        """
        if node.left.left is not None:
            smallest = self.take_smallest(node.left)
        else:
            smallest = node.left
            node.left = None

        node.update_height()
        rebalance(node)
        return smallest

    def take_predecessor(self, node: Node) -> Node:
        """
        Removes the predecessor of node and updates/rebalance accordingly
        :param node: the root of the requested predecessor
        :return: the predecessor of the node
        """
        if node.left.right is None:
            predecessor = node.left
        else:  # the left subtree has a right subtree
            predecessor = self.take_largest(node.left)

        predecessor.update_height()
        predecessor.rebalance()
        return predecessor

    def take_largest(self, node: Node) -> Node:
        """
        Removes the largest node of the subtree rooted at node and
        update/rebalance accordingly
        :param node: the root of the subtree to be operated on
        :return: the largest node of the subtree rooted at node
        """
        if node.right.right is not None:
            largest = self.take_largest(node.right)
        else:
            largest = node.right
            node.right = None

        node.update_height()
        rebalance(node)
        return largest

    def inorder_key(self, node: Node) -> List[str]:
        """
        :param node: the root of the subtree to iterate through
        :return: a list that holds the string representation of the
        keys in the tree by inorder traversal, where "X" denotes no node
        """
        if node is None:
            return []
        elif node.left is None and node.right is None:
            return [node.key]
        else:
            inorder_key = []
            if node.left is not None:
                inorder_key += self.inorder_key(node.left)
            inorder_key += [node.key]
            if node.right is not None:
                inorder_key += self.inorder_key(node.right)
            return inorder_key

    def preorder_key(self, node: Node) -> List[str]:
        """
        :param node: the root of the subtree to iterate through
        :return: a list that holds the string representation of the
        keys in the tree by preorder traversal, where "X" denotes no node
        """
        if node is None:
            return []
        preorder_key = [node.key]
        if node.left is not None:
            preorder_key.extend(self.preorder_key(node.left))
        if node.right is not None:
            preorder_key.extend(self.preorder_key(node.right))
        return preorder_key

    def human_key(self, node: Node) -> Union[list, str]:
        """
        :param node: the root of the subtree to iterate through
        :return: a list that holds the string representation of the
        keys in the tree by preorder traversal, where "X" denotes no node,
        and the depth of the list denotes the depth of the tree.
        """
        if node is None:
            return "X"
        preorder_key = ["X", node.key, "X"]
        if node.left is not None:
            preorder_key[0] = self.human_key(node.left)
        if node.right is not None:
            preorder_key[2] = self.human_key(node.right)
        return preorder_key

    def human_bf(self, node: Node) -> Union[list, str]:
        """
        :param node: the root of the subtree to iterate through
        :return: a list that holds the string representation of the bf
        of the nodes in the tree by preorder traversal, where "X" denotes
        no node, and the depth of the list denotes the depth of the tree.
        """
        if node is None:
            return 'X'
        preorder_key = ['X', node.get_bf(), 'X']
        if node.left is not None:
            preorder_key[0] = self.human_bf(node.left)
        if node.right is not None:
            preorder_key[2] = self.human_bf(node.right)
        return preorder_key

    def human_height(self, node: Node) -> Union[list, str]:
        """
        :param node: the root of the subtree to iterate through
        :return: a list that holds the string representation of the height
        of the nodes in the tree by preorder traversal, where "X" denotes
        no node, and the depth of the list denotes the depth of the tree.
        """

        if node is None:
            return 'X'
        preorder_key = ['X', node.get_height(), 'X']
        if node.left is not None:
            preorder_key[0] = self.human_height(node.left)
        if node.right is not None:
            preorder_key[2] = self.human_height(node.right)
        return preorder_key


def rotate_right(parent: Node, node: Node) -> None:
    """
    :param parent: the parent node of the root of the subtree to be rotated
    :param node: the root of the subtree to be rotated
    """
    if node == parent.left:
        parent.left = node.left
        root = parent.left
    else:  # node == parent.right:
        parent.right = node.left
        root = parent.right

    node.left = None
    root.right, node.left = node, root.right

    if root.right is not None:
        root.right.update_height()
    if root.left is not None:
        root.left.update_height()
    root.update_height()


def rotate_left(parent: Node, node: Node) -> None:
    """
    :param parent: the parent node of the root of the subtree to be rotated
    :param node: the root of the subtree to be rotated
    """
    if node == parent.left:
        parent.left = node.right
        root = parent.left
    else:  # node == parent.right:
        parent.right = node.right
        root = parent.right

    node.right = None
    root.left, node.right = node, root.left

    if root.right is not None:
        root.right.update_height()
    if root.left is not None:
        root.left.update_height()
    root.update_height()


def rebalance(node: Node) -> None:
    """
    :param node: the root of the subtree to rebalance
    """
    for child in [node.left, node.right]:
        if child is None or abs(child.get_bf()) <= 1:
            continue

        if child.get_bf() > 1:
            if child.right.get_bf() < 0:
                rotate_right(child, child.right)
            rotate_left(node, child)
        else:  # child.get_bf() < -1
            if child.left.get_bf() > 0:
                rotate_left(child, child.left)
            rotate_right(node, child)
        node.update_height()
