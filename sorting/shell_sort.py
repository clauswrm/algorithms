""" An implementation of shell sort aka gap sort. """
__author__ = 'Claus Martinsen'


def shell_sort(lst):
    """
    An in-place sorting algorithm that sorts the list in increasing
    order.

    The algorithm starts by sorting pairs of elements far apart from each other,
    then progressively reduces the gap between elements to be compared.

    Starting with far apart elements, it can move some out-of-place elements
    into position faster than a simple nearest neighbor exchange.

    :param lst: An unsorted list of sortable items (i.e. the items can be
     compared using the 'greater-than' operator [>]).
    :type lst: list
    :return: The list sorted in increasing order.
    :rtype: list
    """
    gaps = [103, 46, 20, 9, 4, 1]
    n = len(lst)

    for gap in gaps:
        for i in range(gap, n):
            j = i
            while j >= gap and lst[j - gap] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
                j -= 1
    return lst


if __name__ == '__main__':
    # Only executed when this module is run directly
    # The following is an example of how to use the algorithm

    l = [10000, 53, 6, 854, 1235, 9865, 234, 532, 268, 2, 778, 232, 1, 43, 78, 2893]
    print(shell_sort(l))
