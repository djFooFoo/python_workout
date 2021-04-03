class SummingNumbers:
    def my_sum(self, *numbers: int) -> int:
        total = 0
        for number in numbers:
            total += number
        return total


summing_numbers = SummingNumbers()
print(summing_numbers.my_sum(1, 2, 3, 4))
