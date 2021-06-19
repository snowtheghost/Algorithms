# TODO: Test height during rotation; Test insertion

import unittest
from typing import Optional

from AVL import AVL
from Node import Node


class TestNode(unittest.TestCase):
    def test_comparison(self):
        self.assertEqual(Node(5), Node(5))
        self.assertNotEqual(Node(4), Node(5))
        self.assertLess(Node(4), Node(5))
        with self.assertRaises(TypeError):
            Node(5) == 5


def check_bst_property(tree, current: Optional[Node] = None):
    if not current:
        current = tree.get_root()
    checked = False
    while not checked:
        if current.left:
            if current.left >= current:
                return False
            if not check_bst_property(tree, current.left):
                return False
        if current.right:
            if current.right < current:
                return False
            if not check_bst_property(tree, current.right):
                return False
        checked = True
    return True


class TestAVL(unittest.TestCase):
    def test_bst_insert_single(self):
        tree = AVL()
        tree.bst_insert(5)
        self.assertEqual(tree.get_root(), Node(5))
        self.assertEqual(tree.get_root().height, 0)

    def test_bst_insert_multiple_property(self):
        tree = AVL()
        tree.bst_insert(5)
        tree.bst_insert(2)
        tree.bst_insert(7)
        tree.bst_insert(6)
        tree.bst_insert(0)
        self.assertTrue(check_bst_property(tree))

    def test_bst_insert_multiple_height(self):
        tree = AVL()
        tree.bst_insert(5)
        tree.bst_insert(2)
        tree.bst_insert(7)
        tree.bst_insert(6)
        tree.bst_insert(0)
        self.assertEqual(tree.get_root().height, 2)
        self.assertEqual(tree.get_root().left.height, tree.get_root().right.height, 1)
        self.assertEqual(tree.get_root().left.left.height, tree.get_root().right.left.height, 0)

    def test_rotate_left_full_root(self):
        tree = AVL()
        tree.bst_insert(5)
        tree.bst_insert(2)
        tree.bst_insert(7)
        tree.bst_insert(6)
        tree.bst_insert(0)
        tree.bst_insert(4)
        tree.bst_insert(9)
        tree.rotate_left(tree.get_root())
        self.assertEqual(tree.preorder(), [7, 5, 2, 0, 4, 6, 9])

    def test_rotate_left_full_internal(self):
        tree = AVL()
        tree.bst_insert(5)
        tree.bst_insert(2)
        tree.bst_insert(7)
        tree.bst_insert(6)
        tree.bst_insert(0)
        tree.bst_insert(4)
        tree.bst_insert(9)
        tree.bst_insert(-1)
        tree.bst_insert(1)
        tree.bst_insert(3)
        tree.rotate_left(tree.get_root().left, tree.get_root())
        self.assertEqual(tree.preorder(), [5, 4, 2, 0, -1, 1, 3, 7, 6, 9])

    def test_rotate_left_incomplete_root(self):
        tree = AVL()
        tree.bst_insert(5)
        tree.bst_insert(7)
        tree.rotate_left(tree.get_root())
        self.assertEqual(tree.preorder(), [7, 5])

    def test_rotate_left_incomplete_internal(self):
        tree = AVL()
        tree.bst_insert(5)
        tree.bst_insert(2)
        tree.bst_insert(7)
        tree.bst_insert(6)
        tree.bst_insert(4)
        tree.rotate_left(tree.get_root().left, tree.get_root())
        self.assertEqual(tree.preorder(), [5, 4, 2, 7, 6])

    def test_rotate_right_full_root(self):
        tree = AVL()
        tree.bst_insert(5)
        tree.bst_insert(2)
        tree.bst_insert(7)
        tree.bst_insert(6)
        tree.bst_insert(0)
        tree.bst_insert(4)
        tree.bst_insert(9)
        tree.rotate_right(tree.get_root())
        self.assertEqual(tree.preorder(), [2, 0, 5, 4, 7, 6, 9])

    def test_rotate_right_full_internal(self):
        tree = AVL()
        tree.bst_insert(5)
        tree.bst_insert(2)
        tree.bst_insert(7)
        tree.bst_insert(6)
        tree.bst_insert(0)
        tree.bst_insert(4)
        tree.bst_insert(9)
        tree.bst_insert(-1)
        tree.bst_insert(1)
        tree.bst_insert(3)
        tree.rotate_right(tree.get_root().left, tree.get_root())
        self.assertEqual(tree.preorder(), [5, 0, -1, 2, 1, 4, 3, 7, 6, 9])

    def test_rotate_right_incomplete_root(self):
        tree = AVL()
        tree.bst_insert(5)
        tree.bst_insert(3)
        tree.rotate_right(tree.get_root())
        self.assertEqual(tree.preorder(), [3, 5])

    def test_rotate_right_incomplete_internal(self):
        tree = AVL()
        tree.bst_insert(5)
        tree.bst_insert(2)
        tree.bst_insert(7)
        tree.bst_insert(6)
        tree.bst_insert(1)
        tree.rotate_right(tree.get_root().left, tree.get_root())
        self.assertEqual(tree.preorder(), [5, 1, 2, 7, 6])

if __name__ == '__main__':
    unittest.main()
