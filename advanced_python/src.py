import random

def random_gen():
    # todo exercise 1
    """Generator that yields random numbers between 10 and 20, stopping when it generates 15."""
    while True:
        # Generate a random number between 10 and 20
        num = random.randint(10, 20)

        # Yield (return) the number if it is not 15
        yield num
        if num == 15:
            break

def decorator_to_str(func):
    # todo exercise 2
    """
    Decorator that forces the wrapped function to return a string value.
    """
    def wrapper(*args, **kwargs):
        # Call the function and convert the result to a string
        return str(func(*args, **kwargs))
    return wrapper



@decorator_to_str
def add(a, b):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b


@decorator_to_str
def get_info(d):
    """
    Retrieve the 'info' value from a dictionary.
    And retrurn the value associated with the 'info' key in the dictionary.
    """
    return d['info']


def ignore_exception(exception):
    # todo exercise 3
    """
    Decorator that ignores a specific exception and returns None if it is raised.
    """
    def decorator(func):
        # Define a wrapper function that calls the original function and catches the specified exception    
        def wrapper(*args, **kwargs):
            # use try and except block to catch the specified exception
            try:
                return func(*args, **kwargs)
            except exception:
                return None
        return wrapper
    return decorator


@ignore_exception(ZeroDivisionError)
def div(a, b):
    """
    This function divides two numbers.

    Parameters:
    a (float): The numerator.
    b (float): The denominator.

    Returns:
    float: The result of the division.
    """
    return a / b


@ignore_exception(TypeError)
def raise_something(exception):
    """
    Raises the given exception.

    Args:
        exception: The exception to be raised.
    """
    raise exception


# # exercise 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap
    
# class CacheDecorator:
#     """Saves the results of a function according to its parameters"""
#     def __init__(self):
#         self.cache = {}

#     def __call__(self, func):
#         def _wrap(*args, **kwargs):
#             key = (func.__name__, args, frozenset(kwargs.items()))
#             if key not in self.cache:
#                 self.cache[key] = func(*args, **kwargs)
#             return self.cache[key]

#         return _wrap


if __name__ == '__main__':
    # Test random_gen function
    print("Testing random_gen function:")
    gen = random_gen()
    try:
        while True:
            print(next(gen))
    except StopIteration:
        pass

    # Test decorator_to_str function
    print("\nTesting decorator_to_str function:")
    print(add(5, 10))  # Should print '15'
    print(f"Type of add: {type(add(5, 10))}") # Should print <class 'str'>


    print(get_info({'info': 'Test'}))  # Should print 'Test'
    print(f"Type of get_info: {type(get_info({'info': 'Test'}))}") # Should print <class 'str'>

    # Test ignore_exception function
    print("\nTesting ignore_exception function:")
    @ignore_exception(ZeroDivisionError)
    def div(a, b):
        return a / b

    print(div(10, 2))  # Should print 5.0
    print(div(10, 0))  # Should print None

    print(raise_something(TypeError))  # Should print None

    # Test CacheDecorator class
    print("\nTesting CacheDecorator class:")
    cache_decorator = CacheDecorator()

    @cache_decorator
    def add(a, b):
        return a + b

    print(add(2, 3))  # Should print 5
    print(add(2, 3))  # Should print 5 (cached result)

    print(div(10, 2))  # Should print 5.0
    print(div(10, 2))  # Should print 5.0 (cached result)

   