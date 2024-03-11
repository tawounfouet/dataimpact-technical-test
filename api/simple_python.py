def remove_null(cat_string):
    # todo exercise 1
    """
    Removes 'NULL' substrings from a comma-separated string.
    """
    substrings = cat_string.split(',')
    non_null_substrings = [substring for substring in substrings if substring != 'NULL']
    return ','.join(non_null_substrings)


def reverse_substrings(cat_string):
    # todo exercise 2
    """
    Reverses the order of substrings in a comma-separated string.
    """
    substrings = cat_string.split(',')
    reversed_substrings = substrings[::-1]
    
    return ','.join(reversed_substrings)


