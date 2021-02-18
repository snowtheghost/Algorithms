from typing import Any, List
from AVLDictionary import AVLDictionary
from HashTableDictionary import HashTableDictionary


class Dictionary:
    dictionary = None

    def __init__(self, strategy: int):
        """
        :param strategy: the strategy to use, where 0 => AVL and 1 => HashTable
        """
        if strategy == 0:
            self.dictionary = AVLDictionary()
        elif strategy == 1:
            self.dictionary = HashTableDictionary()
        else:
            print("Invalid strategy")

    def __str__(self) -> str:
        return str(self.dictionary)

    def insert(self, key: Any, value: Any) -> None:
        """
        :param key: the key of the Node to be inserted
        :param value: the value of the Node to be inserted
        """
        self.dictionary.insert(key, value)

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
        return self.dictionary.search(key)

    def delete(self, key: Any) -> None:
        """
        Precondition: key is in dictionary
        :param key: the key to be deleted from the dictionary
        """
        self.dictionary.delete(key)

    def print(self):
        self.dictionary.print()

if __name__ == '__main__':
    # Normal case testing and debugging
    dictionary0 = Dictionary(0)
    dictionary0.insert_all([[5, "five"], [6, "six"], [1, "one"], [3, "three"],
                            [12, "twelve"], [13, "thirteen"], [11, "eleven"]])
    dictionary0.print()
    print(dictionary0.search(5))
    dictionary0.delete(12)
    dictionary0.print()

    dictionary1 = Dictionary(1)
    dictionary1.insert_all([[5, "five"], [6, "six"], [1, "one"], [3, "three"],
                            [12, "twelve"], [13, "thirteen"], [11, "eleven"]])
    dictionary1.print()
    print(dictionary1.search(6))
    dictionary1.delete(12)
    dictionary1.print()