class MaxHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def insert(self, x: int) -> None:
        """
        insert an integer x into the max-heap
        :param x: the value to insert
        """
        i = len(self.heap)  # the index of the item to be inserted
        self.heap.append(x)
        self.bubble_up(i)

    def insert_all(self, items: list) -> None:
        for x in items:
            self.insert(x)

    def bubble_up(self, i: int) -> None:
        """
        bubble up the item at index i to a position that abides by the heap invariant
        :param i: the index of the item to bubble up
        """
        parent = (i - 1) // 2
        if i != 0 and self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.bubble_up(parent)

    def extract_max(self) -> int:
        """
        extract the maximum value in the heap
        :return: the maximum value in the heap
        """
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)

        self.bubble_down(0)

    def bubble_down(self, i: int) -> None:
        """
        bubble down the item at index i to a position that abides by the heap invariant
        :param i: the index of the item to bubble down
        """
        left_child = (i + 1) * 2 - 1
        right_child = (i + 1) * 2

        if left_child >= len(self.heap):
            return

        if right_child >= len(self.heap) or self.heap[left_child] >= self.heap[right_child]:
            max_child = left_child
        else:
            max_child = right_child

        if self.heap[i] < self.heap[max_child]:
            self.heap[i], self.heap[max_child] = self.heap[max_child], self.heap[i]
            self.bubble_down(max_child)


if __name__ == "__main__":
    heap = MaxHeap()
    print(heap)
    heap.insert_all([20, 9, 18, 8, 6, 5, 12, 3, 2])
    print(heap)
    # heap.extract_max()
    # print(heap)
    heap.insert(11)
    print(heap)