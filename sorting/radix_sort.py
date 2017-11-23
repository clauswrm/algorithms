""" An implementation of the O(n) sorting algorithm (lsd) radix-sort. """
__author__ = 'Claus Martinsen'


def radix_sort(lst, digits):
    """
    Sorts a list of decimal integers in linear running-time by sorting by each
    digit, from least significant to most significant. The upper bound is given as
    10^(digits) - 1, and all numbers has to be less than this for the algorithm
    to be correct.
    
    For example, lists with 9999 or 1234 as the greatest element should both
    have digits=4, where as if the greatest element was 666, it should be digits=3.

    This implementation uses counting-sort to sort the numbers by each digit,
    but any stable sorting algorithm will do.

    :param lst: A list of decimal integers.
    :type lst: list
    :param digits: Number of digits in the greatest element in the list -- that
     is, this parameter *must* be equal or greater than ceil(log10(max(lst))).
    :type digits: int
    :return: The list sorted in ascending order.
    :rtype: list
    """
    length = len(lst)
    for digit in range(digits):  # Numbers have size up-to 10^(digits) - 1
        lst = counting_sort(lst, length, digit)
    return lst


def counting_sort(lst, lenght, position, base=10):
    """
    Sorts a list of integers by their digit at the given position. This is 
    implemented by counting the occurrences of the numbers 0 to base - 1, and
    placing the numbers back in a list accordingly.

    :param lst: A list of integers
    :type lst: list
    :param lenght: The length of the list to be sorted.
    :type lenght: int
    :param position: The position of the digit the numbers will be sorted by.
    :type position: int
    :param base: The base of the numbers in the list, default 10 -- decimal.
    :type base: int
    :return: The list sorted by digit number 'position'.
    :rtype: list
    """
    count_lst = [0] * base
    out_lst = [0] * lenght
    
    for number in lst:  # Count all instances of numbers from 0 to base - 1
        d = (number // base ** position) % base  # Extracts the digit at the curent position from each number
        count_lst[d] += 1
        
    for j in range(1, base):  # Accumulate relative index placement
        count_lst[j] += count_lst[j - 1]
        
    for number in reversed(lst):  # Place numbers
        d = (number // base ** position) % base
        count_lst[d] -= 1
        out_lst[count_lst[d]] = number
    return out_lst
