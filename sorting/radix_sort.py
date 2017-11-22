def radix_sort(lst, digits):
    """
    Sorts a list of decimal integers in linear running-time by exploiting the
    fact that we know their upper bound. The upper bound is given as
    10^(digits - 1), and all numbers has to be less than this for the algorithm
    to be correct.

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
    for digit in range(digits):  # Numbers have size up-to 10^(digits - 1)
        lst = countingSort(lst, length, digit)
    return lst


def counting_sort(lst, lenght, position, base=10):
    """
    Sorts a list of integers by counting the occurrences of the numbers 0 to 
    base - 1.
    
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
    countLst = [0] * base
    outLst = [0] * lenght
    for number in lst:  # Count all instances of numbers from 0 to base - 1
        d = (number // base ** position) % base  # Extracts the digit at the curent position from each number
        countLst[d] += 1
    for j in range(1, base):  # Accumulate relative index placement
        countLst[j] += countLst[j - 1]
    for number in reversed(lst):  # Place numbers
        d = (number // base ** position) % base
        countLst[d] -= 1
        outLst[countLst[d]] = number

    return outLst
