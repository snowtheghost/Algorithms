from typing import Any, List, Optional


class MaxHeap:
    def __init__(self, items: Optional[List[int]] = None):
        """
        Initializes a MaxHeap. If items are passed, max heapify the list.
        :param items: An optional list of items to transfer into a max heap.
        """
        if items is None:
            self.heap = []
            self.size = 0
        else:
            self.heap = items
            self.size = len(items)

            for i in reversed(range(self.size)):
                self.bubble_down(i)

    def __str__(self):
        return str(self.heap)

    def get_heap(self) -> list:
        """
        :return: the heap list limited by its size
        """
        return self.heap[:self.size]

    def get_size(self) -> int:
        return self.size

    def bubble_up(self, i: int) -> None:
        """
        bubble up the item at index i to a position that abides by the heap invariant
        :param i: the index of the item to bubble up
        """
        parent = (i - 1) // 2
        if i != 0 and self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.bubble_up(parent)

    def bubble_down(self, i: int) -> None:
        """
        bubble down the item at index i to a position that abides by the heap invariant
        :param i: the index of the item to bubble down
        """
        left_child = (i + 1) * 2 - 1
        right_child = (i + 1) * 2

        if left_child >= self.size:
            return

        if right_child >= self.size or self.heap[left_child] >= self.heap[right_child]:
            max_child = left_child
        else:
            max_child = right_child

        if self.heap[i] < self.heap[max_child]:
            self.heap[i], self.heap[max_child] = self.heap[max_child], self.heap[i]
            self.bubble_down(max_child)

    def heap_sort(self) -> list:
        """
        Sorts the heap list into a normal sorted list. This renders the heap useless.
        :return: the heap list in sorted non-descending order
        """
        initial_size = self.size
        while self.size > 0:
            self.heap[self.size - 1], self.heap[0] = self.heap[0], self.heap[self.size - 1]
            self.size -= 1
            self.bubble_down(0)
        return self.heap[:initial_size]
