""" General and special implementations of bucket sort. """
__author__ = 'Claus Martinsen'


def bucket_sort_0_1(lst):
    """
    TBC
    
    :param lst: An unsorted list of numbers between 0 and 1
    :return:
    """
    n = len(lst)
    buckets = [[] for _ in range(n)]
    for num in lst:
        buckets[int(n * num)].append(num)

    sorted_list = [] #TODO: use the same list
    for bucket in buckets:
        if bucket:  # Do not sort empty lists
            sorted_list += insertion_sort(bucket)  # Add the sorted bucket to the sorted list
    return sorted_list


def bucket_sort_general(lst, mapping):
    """
    TBC

    :param lst: An unsorted list of items that...
    :param mapping:
    :return:
    """
    n = len(lst)
    buckets = [[] for _ in range(n)]
    for num in lst:
        buckets[mapping(num) * n].append(num)

    sorted_list = []
    for bucket in buckets:
        if bucket:  # Do not sort empty lists
            sorted_list += insertion_sort(bucket)  # Add the sorted bucket to the sorted list
    return sorted_list


if __name__ == '__main__':
    # Only executed when this module is run directly
    # The following is an example of how to use the algorithm

    l = [0.461, 0.059, 0.338, 0.649, 0.886, 0.585, 0.971, 0.404, 0.836, 0.185]
    print(bucket_sort_0_1(l))
