""" Calculations helper. """

def get_smallest_positive_integer_not_in_list(numbers: list[int]) -> int:
    """ Calculate the smallest positive integer not in a list of numbers. """
    num_set = set(numbers)  # O(n)
    min_num = 2

    if 1 not in num_set:  # O(1)
        return 1

    while min_num in num_set:  # O(n)
        min_num += 1
    return min_num
