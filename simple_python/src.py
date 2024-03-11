def remove_null(cat_string):
    # todo exercise 1
    """
    Removes 'NULL' substrings from a comma-separated string.
    """
    # Split the string into substrings
    substrings = cat_string.split(',')

    # Create a new list of substrings that do not contain 'NULL' using a list comprehension
    non_null_substrings = [substring for substring in substrings if substring != 'NULL']
    return ','.join(non_null_substrings)


def reverse_substrings(cat_string):
    # todo exercise 2
    """
    Reverses the order of substrings in a comma-separated string.
    """
    # Split the string into substrings
    substrings = cat_string.split(',')

    # Reverse the order of the substrings
    reversed_substrings = substrings[::-1]
    
    return ','.join(reversed_substrings)



def find_missing_number(l):
    # todo exercise 3
    """
    Finds the missing number in a list of integers within a specified range.
    """

    # Get the length of the list
    print(l)
    n = len(l) + 1 #  Add 1 to the length to account for the missing number
    print(n)

    # Calculate the sum of all the numbers in the range
    total_sum = n * (n + 1) // 2 # n(n + 1)/2 is the sum of the first n natural numbers where (n + 1) is the last number in the range
    print(total_sum)

    # Calculate the actual sum of the numbers in the list
    actual_sum = sum(l)
    print(actual_sum)
    
    return total_sum - actual_sum

if __name__ == '__main__':
    #print(remove_null('1,NULL,2,NULL,3')) # '1,2,3'
    #print(reverse_substrings('1,NULL,2,NULL,3')) # '3,NULL,2,NULL,1'
    print(find_missing_number([1, 2, 3, 4, 6, 7, 8])) # 5