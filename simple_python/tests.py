from simple_python.src import remove_null, reverse_substrings, find_missing_number


def test_remove_null():
    assert remove_null('2076,3B,19C,138D,NULL,NULL') == '2076,3B,19C,138D'


def test_reverse_substrings():
    assert reverse_substrings('2076,3B,19C,138D') == '138D,19C,3B,2076'


def test_find_missing_number():
    assert find_missing_number([8, 6, 3, 4, 2, 7, 1]) == 5
    assert find_missing_number([3, 1, 2, 5]) == 4
