""" Quicksort implementations with/without random choice of pivot. """
__author__ = 'Claus Martinsen'

from random import randint


def quick_sort(lst, start, end):
    """
    Sorts the list from index 'start' to index 'end' in-place. The entire list
    is sorted by calling quick_sort(list, 0, len(list) - 1).

    Worst case performance arises by calling the function on a sorted or
    reverse sorted list.

    :param lst: The list to be sorted.
    :type lst: List
    :param start: Starting (left) index of the interval to be sorted.
    :type start: int
    :param end: Ending (right) index of the interval to be sorted.
    :type end: int
    :return: The list sorted, in ascending order.
    :rtype: list
    """
    if start < end:
        p = partition(lst, start, end)
        quick_sort(lst, start, p)
        quick_sort(lst, p + 1, end)
    return lst


def randomized_quick_sort(lst, start, end):
    """
    Sorts the list from index 'start' to index 'end' in-place. The entire list
    is sorted by calling randomized_quick_sort(list, 0, len(list) - 1).

    Fixes quick sorts normal flaw, that worst case performace arises when
    called on a sorted or almost sorted list. This is solved by chosing a
    random pivot.

    :param lst: The list to be sorted.
    :type lst: List
    :param start: Starting (left) index of the interval to be sorted.
    :type start: int
    :param end: Ending (right) index of the interval to be sorted.
    :type end: int
    :return: The list sorted, in ascending order.
    :rtype: list
    """
    if start < end:
        p = randomized_partition(lst, start, end)
        randomized_quick_sort(lst, start, p)
        randomized_quick_sort(lst, p + 1, end)
    return lst


def partition(lst, start, end):
    """
    Partitions the list from index 'start' to index 'end' by choosing the last
    element as a pivot.

    Partitions all smaller elements to the left and all greater or equal
    elements to the right of the pivot. Based on Hoares partition scheme.

    :return: The pivot index.
    :rtype: int
    """
    x = lst[start]
    i = start - 1
    j = end + 1
    while True:
        i += 1
        while lst[i] < x:
            i += 1
        j -= 1
        while lst[j] > x:
            j -= 1

        if i >= j:
            return j

        lst[i], lst[j] = lst[j], lst[i]


def randomized_partition(lst, start, end):
    """
    Partitions the list from index 'start' to index 'end' by choosing a random
    index as a pivot by taking the median of three random elements, greatly
    reducing the probability of worst case performance.

    Partitions all smaller elements to the left and all greater or equal
    elements to the right of the pivot.

    :return: The pivot index.
    :rtype: int
    """
    p = median_of_three(lst, start, end)
    lst[p], lst[end] = lst[end], lst[p]
    return partition(lst, start, end)


def median_of_three(lst, start, end):
    """ Returns index of the median of three randomly chosen list elements. """
    a, b, c = randint(start, end), randint(start, end), randint(start, end)
    if lst[a] <= lst[b] <= lst[c] or lst[a] >= lst[b] >= lst[c]:
        return b
    elif lst[b] <= lst[a] <= lst[c] or lst[b] >= lst[a] >= lst[c]:
        return a
    else:
        return c


if __name__ == '__main__':
    # Only executed when this module is run directly
    # The following is an example of how to use the algorithm

    l1 = [randint(0, 1000) for i in range(1000)]
    l2 = [randint(0, 1000) for i in range(1000)]

    quick_sort(l1, 0, len(l1) - 1)
    randomized_quick_sort(l2, 0, len(l2) - 1)
