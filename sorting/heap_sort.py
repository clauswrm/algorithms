""" Heap and priority queue implementation. """
__author__ = 'Claus Martinsen'


class Heap:
    """ A general purpose heap data structure. Wraps a normal list. """

    def __init__(self, lst, heap_size=-1):
        self.list = lst
        self.heap_size = heap_size
        if heap_size < 0:
            self.heap_size = len(lst)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, index):
        return self.list[index]

    def __setitem__(self, index, value):
        self.list[index] = value

    def __iter__(self):
        return self.list.__iter__()

    def __str__(self):
        return '<Heap:' + str(self.list) + '>'

    def __repr__(self):
        return '<Heap: heap_size=' + str(self.heap_size) + ', length=' + str(len(self)) + '>'

    @staticmethod
    def parent(i):
        return i // 2

    @staticmethod
    def left_child(i):
        return 2 * i

    @staticmethod
    def right_child(i):
        return 2 * i + 1

    def get_maximum(self):
        """ Returns the top of the heap. """
        return self.list[0]

    def heap_extract_max(self):
        """ Pops the top element of the heap, reducing the heap size by one. """
        _max = self.list[0]
        self.list[0] = self.list[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(self.list, 0)
        return _max

    def max_heapify(self, heap, i):
        """ Maintains the max heap property for element 'i'. """
        l, r = self.left_child(i), self.right_child(i)
        if l < self.heap_size and self[l] > self[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self[r] > self[largest]:
            largest = r
        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.max_heapify(heap, largest)


def heap_sort(lst):
    """
    Sorts the list in-place by constructing a max heap.

    :param lst: The list to be sorted.
    :type lst: list
    :return: The list sorted in ascending order.
    :rtype: list
    """
    heap = build_max_heap(lst)
    for i in range(heap.heap_size - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heap.heap_size -= 1
        heap.max_heapify(heap, 0)
    return heap.list


def build_max_heap(lst):
    """ Builds a max heap from the list. """
    heap = Heap(lst)
    for i in range(len(lst) // 2, -1, -1):
        heap.max_heapify(heap, i)
    return heap


if __name__ == '__main__':
    # Only executed when this module is run directly
    # The following is an example of how to use the algorithm

    a = [7, 6, 2, 5, 4, 3, 1]
    print(heap_sort(a))
