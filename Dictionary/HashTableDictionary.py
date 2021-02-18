from typing import Any, List

from HashTable import HashTable


class HashTableDictionary:
    dictionary = HashTable(10)

    def __str__(self) -> str:
        return str(self.dictionary)

    def insert(self, key: int, value: Any) -> None:
        """
        :param key: the key of the Item to be inserted
        :param value: the value of the Item to be inserted
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
        print(self.dictionary)


if __name__ == '__main__':
    # Normal case testing and debugging
    dictionary = HashTableDictionary()
    dictionary.insert_all([[5, "five"], [6, "six"], [1, "one"], [3, "three"],
                           [12, "twelve"], [13, "thirteen"], [11, "eleven"]])
    dictionary.print()
    print(dictionary.search(6))
    dictionary.delete(12)
    dictionary.print()