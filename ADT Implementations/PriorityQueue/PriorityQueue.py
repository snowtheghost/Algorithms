from typing import List, Any, Union


class PriorityQueue:
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
