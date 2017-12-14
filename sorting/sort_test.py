""" A test for sorting algorithms. """
__author__ = 'Claus Martinsen'

from timeit import default_timer as timer
import matplotlib.pyplot as plot
from time import sleep
from random import randrange
from collections import Callable

from algo_repo.sorting.quick_sort import quick_sort
from algo_repo.sorting.merge_sort import merge_sort
from algo_repo.sorting.heap_sort import heap_sort
from algo_repo.sorting.radix_sort import radix_sort
from algo_repo.sorting.bucket_sort import bucket_sort_general


def test(sort_algo, array_size):
    """
    Tests a sorting algorithm.

    :param sort_algo: The sorting algorithm to be tested.
    :type sort_algo: Callable
    :param array_size: The size of the array to be sorted.
    :type array_size: int
    :return: Total sorting time.
    :rtype: int
    """
    max_element = 1000
    array = [randrange(0, max_element) for _ in range(array_size)]
    sleep(0.1)  # Let the system settle a bit

    if sort_algo.__name__ == 'quick_sort':
        start_time = timer()
        array = sort_algo(array, 0, array_size - 1)
        total_time = timer() - start_time
    elif sort_algo.__name__ == 'radix_sort':
        start_time = timer()
        array = sort_algo(array, 3)
        total_time = timer() - start_time
    elif sort_algo.__name__ == 'bucket_sort_general':
        def mapper(n):
            return n / max_element

        start_time = timer()
        array = sort_algo(array, mapper)
        total_time = timer() - start_time
    else:
        start_time = timer()
        array = sort_algo(array)
        total_time = timer() - start_time

    try:
        verify(array)
    except ValueError as sorting_fail:
        print('Sorting algorithm "' + sort_algo.__name__ + '" failed to sort list in ascending order.')
        print(sorting_fail)
    return total_time


def verify(array):
    """ Verifies that the array is sorted. """
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            raise ValueError('Unsorted list detected. (' + str(array[i - 1]) + ' > ' + str(array[i]) + ')')


def display_results(results, sizes):
    """ Plots the resulting running times. """
    plot.xlabel('Array size')
    plot.ylabel('Time')
    plot.title('Sorting algorithms comparison')
    for name, result in results.items():
        plot.plot(sizes, result, label=name)
    plot.grid(True)
    plot.legend()
    plot.show()


def main():
    """ Tests all sorting algorithms for a variety of array sizes and displays the result. """
    algos = [merge_sort, quick_sort, heap_sort, radix_sort, bucket_sort_general]
    array_sizes = [5000, 10000, 15000, 20000, 50000, 75000, 100000, 150000]
    results = {algo.__name__: [] for algo in algos}
    for algo in algos:
        result = []
        for size in array_sizes:
            time = test(algo, size)
            result.append(time)
        results[algo.__name__] = result

    display_results(results, array_sizes)


if __name__ == '__main__':
    main()
