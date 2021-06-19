from typing import Any, Optional


class Queue:
    queue = []

    def enqueue(self, item: Any) -> None:
        self.queue.append(item)

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def dequeue(self) -> Optional[Any]:
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)


if __name__ == '__main__':
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print(q.dequeue())
    q.enqueue("d")
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())
    print(q.dequeue())
    print(q.is_empty())
    print(q.dequeue())