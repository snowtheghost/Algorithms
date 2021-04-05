from typing import Any


class Node:
    item = None
    next = None

    def __init__(self, item: Any):
        self.item = item

    def __str__(self):
        return str(self.item)


class LinkedList:
    root = None
    current_node = root

    def __str__(self):
        if self.root is None:
            return str([])

        items = []
        current_node = self.root
        while current_node is not None:
            items.append(current_node.item)
            current_node = current_node.next
        return str(items)

    def __iter__(self):
        self.current_node = self.root
        return self

    def __next__(self):
        if self.current_node is not None:
            item = self.current_node.item
            self.current_node = self.current_node.next
            return item
        else:
            raise StopIteration

    def __contains__(self, item: Any) -> bool:
        current_node = self.root
        while current_node is not None:
            if current_node.item == item:
                return True
            else:
                current_node = current_node.next
        return False

    def __len__(self):
        current_node = self.root
        counter = 0
        while current_node is not None:
            counter += 1
            current_node = current_node.next
        return counter

    def insert(self, item: Any, node: Node = root) -> None:
        new_node = Node(item)

        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        
    def insert_all(self, items: list) -> None:
        for item in items:
            self.insert(item)

    def insert_first(self, item) -> None:
        new_node = Node(item)
        if self.root is None:
            self.root = new_node
        else:
            new_node.next = self.root
            self.root = new_node

    def delete(self, item: Any) -> None:
        if self.root.item == item:
            self.root = self.root.next
            return

        current_node = self.root
        while current_node.next is not None:
            if current_node.next.item == item:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next


if __name__ == '__main__':
    items = LinkedList()
    print(items)
    items.insert_all([4, 7, 2, 3, 0, 6, 5])
    print(items)
    items.delete(6)
    print(items)
    items.insert_first(9)
    print(items)

    for item in items:
        print(item)
