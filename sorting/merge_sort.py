""" An implementation of the divide-and-conquer sorting algorithm merge sort. """
__author__ = 'Claus Martinsen'


def merge_sort(lst, start=0, end=-1):
    """
    Sorts a list of compareable elements by dividing the list until at lists
    with length 1, then merging two and two lists together.

    :param lst: An unsorted list of compareable elements.
    :type lst: list
    :param start: Start (left) index.
    :type start: int
    :param end: End (right) index.
    :type end: int
    :return: The list sorted in increasing order.
    :rtype: list
    """
    if end < 0:  # If called with no end parameter
        end = len(lst) - 1
    if start == end:  # Base-case, return the single element
        return [lst[start]]

    middle = (start + end) // 2
    leftList = merge_sort(lst, start, middle)
    rightList = merge_sort(lst, middle + 1, end)

    return merge(leftList, middle - start + 1, rightList, end - middle)


def merge(list_a, length_a, list_b, length_b):
    """
    Merges two lists together by always choosing the smaller of the two values
    from the front of the lists. When one list is exhausted, the other list has
    simply all its elements added to the end of the merged list.
    """
    index_a, index_b = 0, 0
    merged_list = []

    while index_a < length_a and index_b < length_b:
        if list_a[index_a] < list_b[index_b]:  # Add the smallest of the two
            merged_list.append(list_a[index_a])
            index_a += 1
        else:
            merged_list.append(list_b[index_b])
            index_b += 1

    if index_a < length_a:  # The list who hasn't reached its end is not exhausted
        merged_list.extend(list_a[index_a:])
    else:
        merged_list.extend(list_b[index_b:])

    return merged_list


if __name__ == "__main__":
    # Only executed when this module is run directly
    # The following is an example of how to use the algorithm

    l = [461, 59, 1024, 338, 649, 886, 8196, 585, 971, 5, 404, 836, 185]
    print(merge_sort(l))
