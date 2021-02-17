from typing import Any, List
from AVL import AVL


class Dictionary:
    dictionary = AVL()

    def __str__(self) -> str:
        """
        :return: a list that holds the string representation of the
        keys in the tree by preorder traversal, where "X" denotes no node,
        and the depth of the list denotes the depth of the tree.
        """
        return str(self.dictionary)

    def insert(self, key: Any, value: Any) -> None:
        """
        :param key: the key of the Node to be inserted
        :param value: the value of the Node to be inserted
        """
        self.dictionary.insert(self.dictionary.root, key, value)

    def insert_all(self, pairs: List[List[Any]]) -> None:
        """
        :param pairs: a list of key/value pairs of the Nodes to be inserted
        """
        for pair in pairs:
            key = pair[0]
            value = pair[1]
            self.insert(key, value)

    def search(self, key: Any) -> Any:
        """
        :param key: the key that is requested to be searched for
        :return: the corresponding value of the key, or None if not present
        """
        return self.dictionary.search(self.dictionary.root, key)

    def delete(self, key: Any) -> None:
        """
        Precondition: key is in dictionary
        :param key: the key to be deleted from the dictionary
        """
        self.dictionary.delete(None, key)

    def print_tree(self):
        """
        :return: a list that holds the string representation of the
        keys in the tree by preorder traversal, where "X" denotes no node,
        and the depth of the list denotes the depth of the tree.
        """
        print(f'Data: {self}')

    def print_height(self):
        """
        :return: a list that holds the string representation of the height
        of the nodes in the tree by preorder traversal, where "X" denotes
        no node, and the depth of the list denotes the depth of the tree.
        """
        print(f'Heights: {self.dictionary.human_height(self.dictionary.root)}')

    def print_bf(self):
        """
        :return: a list that holds the string representation of the bf
        of the nodes in the tree by preorder traversal, where "X" denotes
        no node, and the depth of the list denotes the depth of the tree.
        """
        print(f'Balance Factors: {self.dictionary.human_bf(self.dictionary.root)}')

    def print(self):
        self.print_tree()
        self.print_height()
        self.print_bf()


if __name__ == '__main__':
    # Normal case testing and debugging
    dictionary = Dictionary()
    dictionary.insert_all([[5, "five"], [6, "six"], [1, "one"], [3, "three"],
                           [12, "twelve"], [13, "thirteen"], [11, "eleven"]])
    dictionary.print()
    print(dictionary.search(5))
    dictionary.delete(12)
    dictionary.print()
