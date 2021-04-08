# A hashtable using a double hashing method to store items (limited to integers)
from typing import Any, Optional

from Item import Item


class HashTable:
    table = []
    size = 0
    capacity = 0

    def __init__(self, size: int):
        """
        Precondition: size >= 10
        :param size: the desired size of the table
        """
        self.size = size
        self.table = [None]*self.size
        self.capacity = self.size

    def __str__(self):
        table = []
        for item in self.table:
            if item is not None:
                table.append(item.get_item())
            else:
                table.append(item)
        return str(table)

    def hash(self, key: int, i: int) -> int:
        """
        :param i: the position to try
        :param key: the key to be hashed
        :return: an integer corresponding to the index on the table
        """
        return (self.hash1(key) + self.hash2(key) * i) % self.size

    def hash1(self, key: int) -> int:
        """
        :param key: the key to be hashed
        :return: an integer corresponding to the first hash of the final hash function
        """
        return key % self.size

    def hash2(self, key: int) -> int:
        """
        :param key: the key to be hashed
        :return: an integer corresponding to the second hash of the final hash function
        """
        return 7 - (key % 7)

    def insert(self, key: int, value: Any) -> None:
        """
        :param value: the value corresponding to the key
        :param key: the key to be inserted
        """
        i = 0
        while self.table[self.hash(key, i)] is not None and self.table[self.hash(key, i)].key() is not None \
                and key != self.table[self.hash(key, i)].key():
            i += 1
        self.table[self.hash(key, i)] = Item(key, value)
        self.capacity -= 1

    def search(self, key) -> Optional[Any]:
        """
        :param key: the key of the requested item
        :return: return None if the key does not exist, else the value of the key
        """
        i = 0
        while self.table[self.hash(key, i)] is not None:
            if self.table[self.hash(key, i)].key() == key:
                return self.table[self.hash(key, i)].value()
            else:
                i += 1
        return None

    def delete(self, key) -> None:
        """
        Precondition: key in self
        :param key: the key to delete
        """
        i = 0
        while self.table[self.hash(key, i)] is not None:
            if self.table[self.hash(key, i)].key() == key:
                self.table[self.hash(key, i)] = Item()
                self.capacity -= 1
                break
            else:
                i += 1


if __name__ == "__main__":
    hashtable = HashTable(10)
    hashtable.insert(5, "five")
    hashtable.delete(5)
    hashtable.insert(5, "new five")
    print(hashtable)
    print(hashtable.search(6))
