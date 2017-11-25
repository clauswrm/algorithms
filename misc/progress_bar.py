""" A console writer for visualizing the progress of a task. """
__author__ = 'Claus Martinsen'

from sys import stdout
from math import floor


def update_progress(current, total, length=10):
    """ Prints a progress bar as well as a percentage to the console. """
    percentage = int(floor((current / total) * 100))
    progress = int(floor((current / total) * length))
    stdout.write('\r[{0}] {1}%'.format('#' * progress + ' ' * (length - progress), percentage))
    stdout.flush()


if __name__ == '__main__':
    # Only executed when this module is run directly
    # The following is an example of how to use the algorithm

    from time import sleep

    t = 100
    for i in range(t + 1):
        sleep(0.1)  # Simulating some work
        update_progress(i, t)
