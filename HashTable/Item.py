from typing import Any, Optional


class Item:
    item = (None, None)

    def __init__(self, key: Optional[int] = None, value: Optional[Any] = None):
        self.item = (key, value)

    def __str__(self):
        return str(self.item)

    def key(self) -> int:
        return self.item[0]

    def value(self) -> Any:
        return self.item[1]

    def get_item(self) -> tuple:
        return self.item
