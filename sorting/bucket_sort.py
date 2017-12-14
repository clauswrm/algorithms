""" General and special implementations of bucket sort. """
__author__ = 'Claus Martinsen'

from algorithms.sorting.insertion_sort import insertion_sort


def bucket_sort_0_1(lst):
    """
    Sorts a list of n floating point numbers between 0 and 1 by placing them
    into one of n buckets based on their value.

    Each bucket is then sorted by using insertion sort (used because of its low
    overhead), but any sorting algorithm would do. The sorted buckets are then
    concatenated to one sorted list.

    :param lst: An unsorted list of numbers between 0 and 1.
    :type lst: list
    :return: The list sorted in increasing order.
    :rtype: list
    """
    n = len(lst)
    buckets = [[] for _ in range(n)]
    for num in lst:
        buckets[int(n * num)].append(num)

    lst.clear()  # Make the list ready for re-use
    for bucket in buckets:
        if bucket:  # Do not sort empty lists
            lst += insertion_sort(bucket)  # Add the sorted bucket to the sorted list
    return lst


def bucket_sort_general(lst, mapping):
    """
    Sorts a list of n compareable elements by placing them into one of n
    buckets based on their value. Each element is mapped to a value between 0
    and 1 based on how big they are by the *mapping* parameter.

    IMPORTANT: The mapping should be reflect the distribution of elements, so
    that each bucket has approximately the same probability of being filled.
    Example: A uniform distribution should have a uniform mapping function,
    and a normal distribution should have a normalized mapping.

    If each bucket does not have the same probability of being filled, the
    average linear running-time will not be certain.

    Each bucket is then sorted by using insertion sort (used because of its low
    overhead), but any sorting algorithm would do. The sorted buckets are then
    concatenated to one sorted list.

    Also known as 'proxmap sort'.

    :param lst: An unsorted list of compareable elements.
    :type lst: list
    :param mapping: A function that takes in an element and outputs a number
     between 0 and 1 indicating how big the number is.
    :type mapping: Callable
    :return: The list sorted in increasing order.
    :rtype: list
    """
    n = len(lst)
    buckets = [[] for _ in range(n)]
    for num in lst:
        buckets[int(mapping(num) * n)].append(num)

    lst.clear()  # Make the list ready for re-use
    for bucket in buckets:
        if bucket:  # Do not sort empty lists
            lst += insertion_sort(bucket)  # Add the sorted bucket to the sorted list
    return lst


if __name__ == '__main__':
    # Only executed when this module is run directly
    # The following is an example of how to use the algorithm

    l1 = [0.461, 0.059, 0.338, 0.649, 0.886, 0.585, 0.971, 0.404, 0.836, 0.185]
    l2 = [34, 68, 234, 876, 1, 46, 987, 32, 147, 567]


    def mapper(n):
        return n / 1000


    print(bucket_sort_0_1(l1))
    print(bucket_sort_general(l2, mapping=mapper))
