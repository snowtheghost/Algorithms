class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class MaxHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        heap_readable = []
        for node in self.heap:
            heap_readable.append((node.value, node.priority))
        return str(heap_readable)

    def insert(self, value, priority: int) -> None:
        """
        insert a node x into the max-heap
        :param value: the item to add
        :param priority: the priority of the item
        """
        i = len(self.heap)  # the index of the item to be inserted
        x = Node(value, priority)
        self.heap.append(x)
        self.bubble_up(i)

    def insert_all(self, items: list) -> None:
        """
        :param items: a list of tuples of format (value, priority)
        """
        for item in items:
            self.insert(item[0], item[1])

    def bubble_up(self, i: int) -> None:
        """
        bubble up the item at index i to a position that abides by the heap invariant
        :param i: the index of the item to bubble up
        """
        parent = (i - 1) // 2
        if i != 0 and self.heap[parent].priority < self.heap[i].priority:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.bubble_up(parent)

    def extract_max(self) -> int:
        """
        extract the maximum value in the heap
        :return: the maximum value in the heap
        """
        max_node = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        self.bubble_down(0)
        return max_node.value

    def bubble_down(self, i: int) -> None:
        """
        bubble down the item at index i to a position that abides by the heap invariant
        :param i: the index of the item to bubble down
        """
        left_child = (i + 1) * 2 - 1
        right_child = (i + 1) * 2

        if left_child >= len(self.heap):
            return

        if right_child >= len(self.heap) or self.heap[left_child].priority >= self.heap[right_child].priority:
            max_child = left_child
        else:
            max_child = right_child

        if self.heap[i].priority < self.heap[max_child].priority:
            self.heap[i], self.heap[max_child] = self.heap[max_child], self.heap[i]
            self.bubble_down(max_child)

    def change_priority(self, x: Node, new_priority: int) -> None:
        """
        :param x: a pointer to the node to edit
        :param new_priority:
        """
        i = self.heap.index(x)
        old_priority = x.priority
        x.priority = new_priority

        if x.priority > old_priority:
            self.bubble_up(i)
        elif new_priority < old_priority:
            self.bubble_down(i)


if __name__ == "__main__":
    heap = MaxHeap()
    print(heap)
    heap.insert_all([("20", 20), ("9", 9), ("18", 18), ("8", 8), ("6", 6), ("5", 5), ("12", 12), ("3", 3), ("2", 2)])
    print(heap)
    # heap.extract_max()
    # print(heap)
    heap.insert("11", 11)
    print(heap)
    heap.change_priority(heap.heap[3], 19)
    print(heap)
    heap.change_priority(heap.heap[4], 3)
    print(heap)