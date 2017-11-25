""" An implementation of the basic sorting algorithm insertion sort. """
__author__ = 'Claus Martinsen'


def insertion_sort(lst):
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
    
    l = [0.461, 0.059, 0.338, 0.649, 0.886, 0.585, 0.971, 0.404, 0.836, 0.185]
    print(bucket_sort_0_1(l))
