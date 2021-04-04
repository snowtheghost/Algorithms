from typing import Any


class DynamicArray:
    """
    Note that although we are implementing dynamic arrays with a python list as opposed to an array, this implementation
    is practice for myself to consolidate the ADT.
    """
    allocated = 1
    size = 0
    array = [None]*allocated  # Not an array, but this will function as an array

    def __str__(self):
        return str(self.array[0:self.size])

    def insert(self, item: Any) -> None:
        """
        if the size will exceed allocated space, increase the allocated space of the array by a factor of 2 and insert.
        :param item: the item to insert

        Average Case: O(1)
        """
        if self.size == self.allocated:
            self.allocated = self.allocated * 2
            new_array = [None]*self.allocated

            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array

        self.array[self.size] = item
        self.size += 1

    def insert_all(self, items: list) -> None:
        for item in items:
            self.insert(item)


if __name__ == '__main__':
    items = DynamicArray()
    print(items)
    items.insert_all([4, 7, 2, 3, 0, 6, 5])
    print(items)
