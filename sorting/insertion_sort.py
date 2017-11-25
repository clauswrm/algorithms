""" An implementation of the basic sorting algorithm insertion sort. """
__author__ = 'Claus Martinsen'


def insertion_sort(lst):
    """
    A stable, in-place sorting algorithm that sorts the list in increasing
    order, one element at a time.

    :param lst: An unsorted list of sortable items (i.e. the items can be
     compared using the 'greater-than' operator [>]).
    :type lst: list
    :return: The list sorted in increasing order.
    :rtype: list
    """
    n = len(lst)
    for i in range(1, n):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
    return lst


if __name__ == '__main__':
    # Only executed when this module is run directly
    # The following is an example of how to use the algorithm
    
    l = [10000,53,6,854,1235,9865,234]
    print(insertion_sort(l))
