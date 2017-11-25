""" A decorator for adding memoization to functions. """
__author__ = 'Claus Martinsen'


def memoize(func):
    """ A decorator to add the dynamic programming principle memoization to a function. """
    memory = dict()
    
    def memoize_func(arg):
        if arg in memory:
            return memory[arg]
        else:
            value = func(arg)
            memory[arg] = value
        return value
    
    return memoize_func


if __name__ == '__main__':
    # Only executed when this module is run directly
    # The following is an example of how to use the decorator
    
    @memoize  # Try running fibonacci(40) with/without this!
    def fibonacci(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    
    print(fibonacci(40))
    # Without memoization -> Exponential running time
    # With memoization -> Linear running time
