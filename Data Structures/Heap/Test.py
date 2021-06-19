import unittest
from random import randint, randrange

from MaxHeap import MaxHeap


def generate_random_list(size: int) -> list:
    random_list = []
    for _ in range(0, size):
        random_list.append(randrange(0, size))
    return random_list


def check_heap_property(heap: list, size: int):
    for i in range(size):
        left = (i + 1) * 2 - 1
        right = (i + 1) * 2
        if left < size:
            if heap[left] > heap[i]:
                return False
        if right < size:
            if heap[right] > heap[i]:
                return False
    return True


class TestMaxHeap(unittest.TestCase):
    def test_init_empty(self):
        max_heap = MaxHeap()
        self.assertEqual(max_heap.get_size(), 0)

    def test_init_max_heapify_defined(self):
        max_heap = MaxHeap([2, 7, 4, 5, 1, 0, 9, 8])
        self.assertTrue(check_heap_property(max_heap.get_heap(), max_heap.get_size()))

    def test_init_max_heapify_random(self):
        max_heap = MaxHeap(generate_random_list(100))
        self.assertTrue(check_heap_property(max_heap.get_heap(), max_heap.get_size()))

    def test_bubble_up(self):
        max_heap = MaxHeap([2, 7, 4, 5, 1, 0, 9, 8])
        max_heap.heap.append(10)
        max_heap.size += 1
        self.assertFalse(check_heap_property(max_heap.get_heap(), max_heap.get_size()))
        max_heap.bubble_up(max_heap.get_size() - 1)
        self.assertTrue(check_heap_property(max_heap.get_heap(), max_heap.get_size()))

    def test_bubble_down(self):
        max_heap = MaxHeap([2, 7, 4, 5, 1, 0, 9, 8])
        max_heap.heap[0] = 3
        self.assertFalse(check_heap_property(max_heap.get_heap(), max_heap.get_size()))
        max_heap.bubble_down(0)
        self.assertTrue(check_heap_property(max_heap.get_heap(), max_heap.get_size()))

    def test_heap_sort_defined(self):
        max_heap = MaxHeap([2, 7, 4, 5, 1, 0, 9, 8])
        self.assertTrue(sorted(max_heap.heap_sort()))

    def test_heap_sort_random(self):
        max_heap = MaxHeap(generate_random_list(100))
        self.assertTrue (sorted(max_heap.heap_sort()))


if __name__ == '__main__':
    unittest.main()
