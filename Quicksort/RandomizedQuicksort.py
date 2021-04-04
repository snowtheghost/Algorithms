from random import randrange


def randomized_quicksort(items: list) -> list:
    """
    :param items: a list of sortable items
    :return: a new list of items in ascending order

    Expected worst case: O(nlog(n))
    """
    if len(items) <= 1:  # Do nothing if the list is not sortable
        return items[:]
    else:
        pivot_index = randrange(0, len(items))
        print(pivot_index)
        pivot = items[pivot_index]  # Choose the pivot to be the first item i
        split = partition(items[:pivot_index] + items[pivot_index+1:], pivot)
        left = split[0]
        right = split[1]
        left = randomized_quicksort(left)
        right = randomized_quicksort(right)
        return left + [pivot] + right


def partition(items: list, pivot: int) -> list:
    """
    :param items: a list of sortable items
    :param pivot: the item chosen as the pivot
    :return: a list of two lists, where the left list contains all items leq to the pivot and the right list contains
    the remaining items
    """
    left = []
    right = []
    for item in items:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)
    return [left, right]


if __name__ == '__main__':
    print(randomized_quicksort([4, 7, 2, 3, 0, 6, 5]))
