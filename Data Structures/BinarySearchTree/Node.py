from typing import Any, Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)
