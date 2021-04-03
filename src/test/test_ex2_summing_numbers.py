import unittest

from assertpy import assert_that

from ex2_summing_numbers import SummingNumbers


class TestSummingNumbers(unittest.TestCase):
    def setUp(self) -> None:
        self.summing_numbers = SummingNumbers()

    def test_without_arguments_returns_zero(self) -> None:
        result = self.summing_numbers.my_sum()

        assert_that(result).is_equal_to(0)

    def test_sums_all_given_arguments(self) -> None:
        result = self.summing_numbers.my_sum(1, 2, 4)

        assert_that(result).is_equal_to(7)


if __name__ == '__main__':
    unittest.main()
