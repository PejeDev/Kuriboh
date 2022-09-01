from app.helpers.calc import get_smallest_positive_integer_not_in_list

def test_get_smallest_positive_integer_not_in_list():
		assert get_smallest_positive_integer_not_in_list([1, 3, 2]) == 4
		assert get_smallest_positive_integer_not_in_list([-1, -3]) == 1
		assert get_smallest_positive_integer_not_in_list([-999, -1, -3]) == 1
		assert get_smallest_positive_integer_not_in_list([]) == 1
		assert get_smallest_positive_integer_not_in_list([1]) == 2
		assert get_smallest_positive_integer_not_in_list([1, 2, 3, 4, 5, 6, 8, 9, 10]) == 7
