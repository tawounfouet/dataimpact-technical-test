import pytest

from src import div, raise_something, add, random_gen, get_info, CacheDecorator


def test_generator():
    g = random_gen()
    assert isinstance(g, type((x for x in [])))
    a = next(g)
    while a != 15:
        assert 10 <= a <= 20
        a = next(g)
    with pytest.raises(StopIteration):
        next(g)


def test_to_str():
    assert add(5, 30) == '35'
    assert get_info({'info': [1, 2, 3]}) == '[1, 2, 3]'


def test_ignore_exception():
    assert div(10, 2) == 5
    assert div(10, 0) is None
    assert raise_something(TypeError) is None
    with pytest.raises(NotImplementedError):
        raise_something(NotImplementedError)


# Define tests for CacheDecorator class
def test_cache_decorator():
    # Create an instance of CacheDecorator
    cache_decorator = CacheDecorator()

    # Define a function to be decorated
    @cache_decorator
    def add_nums(a, b):
        return a + b

    # Test caching behavior
    # The result of add_nums(2, 3) should be cached
    assert add_nums(2, 3) == 5
    # The cached result should be returned without calling the function again
    assert add_nums(2, 3) == 5
    # The cache should store the result for each unique set of arguments
    assert add_nums(4, 5) == 9

    # Test clearing cache
    cache_decorator.cache.clear()
    # The cache should be empty after clearing
    assert len(cache_decorator.cache) == 0

    # Test caching behavior with another function (div)
    @cache_decorator
    def divide_nums(a, b):
        return a / b

    # The result of divide_nums(10, 2) should be cached
    assert divide_nums(10, 2) == 5.0
    # The cached result should be returned without calling the function again
    assert divide_nums(10, 2) == 5.0
    # The cache should store the result for each unique set of arguments
    assert divide_nums(20, 4) == 5.0

    # Test caching behavior with a function that raises an exception (raise_something)
    @cache_decorator
    def raise_exception():
        return raise_something(ValueError)

    # The function should raise an exception, but the result should still be cached
    with pytest.raises(ValueError):
        raise_exception()
    # The cached result should be returned without calling the function again
    with pytest.raises(ValueError):
        raise_exception()