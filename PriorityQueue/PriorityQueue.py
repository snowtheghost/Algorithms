from typing import List, Any, Union


class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class MinPriorityQueue:
    def __init__(self):
        self.heap = []

    def __str__(self):
        out_list = []
        for node in self.heap:
            out_list.append((node.value, node.priority))
        return str(out_list)

    def __contains__(self, item: Any):
        for node in self.heap:
            if node.value == item:
                return True
        return False

    def bubble_up(self, index: int) -> None:
        parent_index = (index - 1) // 2  # integer division
        while parent_index >= 0 and self.heap[parent_index].priority > self.heap[index].priority:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def bubble_down(self, index: int) -> None:  # TODO: Optimize
        child_index = [(index + 1) * 2 - 1, (index + 1) * 2]
        if child_index[0] >= len(self.heap):
            return

        if child_index[1] >= len(self.heap) or self.heap[child_index[0]].priority < self.heap[child_index[1]].priority:
            max_child_index = child_index[0]
        else:
            max_child_index = child_index[1]
        if self.heap[index].priority > self.heap[max_child_index].priority:
            self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]
            index = max_child_index
            self.bubble_down(index)

    def insert(self, value: Any, priority: Union[int, float]):
        new_node = Node(value, priority)
        self.heap.append(new_node)
        self.bubble_up(len(self.heap) - 1)

    def insert_all(self, items: List[tuple]):
        for item in items:
            self.insert(item[0], item[1])

    def extract_min(self) -> Node:
        max_priority = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
        else:
            self.heap[0] = self.heap.pop()
            self.bubble_down(0)
        return max_priority

    def delete(self, item: Any) -> None:
        i = 0
        while i < len(self.heap):
            if self.heap[i].value == item:
                if i == len(self.heap) - 1:
                    self.heap.pop()
                else:
                    self.heap[i] = self.heap.pop()
                    self.bubble_down(i)
                break
            i += 1

    def update_priority(self, item: Any, new_priority: Union[int, float]):
        self.delete(item)
        self.insert(item, new_priority)

    def is_empty(self) -> bool:
        return len(self.heap) == 0


if __name__ == "__main__":
    heap = MinPriorityQueue()
    print(heap.is_empty())

    heap.insert_all([("a", 9), ("b", 20), ("c", 8) , ("d", 18), ("e", 6), ("f", 5), ("g", 12)])
    print(heap)

    heap.insert("h", 22)
    print(heap)

    heap.extract_min()
    print(heap)

    heap.delete("a")
    print(heap)

    heap.update_priority("d", 5)
    print(heap)
