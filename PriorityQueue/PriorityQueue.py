from typing import List


class PriorityQueue:
    heap = []

    def __init__(self):
        pass

    def __str__(self):
        return str(self.heap)

    def bubble_up(self, index: int) -> None:
        parent_index = (index - 1) // 2  # integer division
        while parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def bubble_down(self, index: int) -> None:  # TODO: Optimize
        child_index = [(index + 1) * 2 - 1, (index + 1) * 2]
        if child_index[0] >= len(self.heap):
            return

        if child_index[1] >= len(self.heap) or self.heap[child_index[0]] > self.heap[child_index[1]]:
            max_child_index = child_index[0]
        else:
            max_child_index = child_index[1]
        if self.heap[index] < self.heap[max_child_index]:
            self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]
            index = max_child_index
            self.bubble_down(index)

    def insert(self, value: int):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)

    def insert_all(self, values: List[int]):
        for value in values:
            self.insert(value)

    def extract_max(self) -> int:
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        return max_value


if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert_all([20, 9, 18, 8, 6, 5, 12, 3, 2])
    heap.insert(11)
    print(heap)
