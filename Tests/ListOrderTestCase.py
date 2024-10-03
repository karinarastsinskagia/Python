import unittest


# Define a function 'is_prime' to check if a number is prime.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, (number//2)+1):
        if number % i == 0:
            return False
    return True

# Define a test case class 'PrimeNumberTestCase' that inherits from 'unittest.TestCase'.
class ListOrderTestCase(unittest.TestCase):

    # Define a test method 'test_prime_numbers' to test prime numbers.
    def test_list_is_sorted_in_ascending(self):
        lst = [1, 2, 3, 4, 5, 6, 7]
        expected_lst = lst
        expected_lst.sort(reverse=False)

        self.assertEqual(expected_lst,lst)

    # Define a test method 'test_non_prime_numbers' to test non-prime numbers.
    def test_list_is_not_sorted_in_ascending(self):
        lst = [5, 7, 2, 8, 1, 9]

        expected_lst = lst.copy()

        expected_lst.sort(reverse=False)

        self.assertNotEqual(expected_lst, lst)


if __name__ == '__main__':
    unittest.main()
