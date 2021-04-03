import builtins
import random
import unittest

from mockito import spy, verify, when

from ex1_number_guessing_game import NumberGuessingGame


class TestNumberGuessingGame(unittest.TestCase):
    def setUp(self) -> None:
        self.random = spy(random)
        self.builtins = spy(builtins)
        self.number_guessing_game = NumberGuessingGame(random=self.random, builtins=self.builtins)

    def test_chooses_random_integer_between_zero_and_hundred(self) -> None:
        when(random).randint(0, 100).thenReturn(42)
        when(builtins).input('What number has been chosen?').thenReturn('42')

        self.number_guessing_game.guessing_game()

        verify(self.random).randint(0, 100)

    def test_takes_user_input(self) -> None:
        when(random).randint(0, 100).thenReturn(11)
        when(builtins).input('What number has been chosen?').thenReturn('11')

        self.number_guessing_game.guessing_game()

        verify(self.builtins).input('What number has been chosen?')

    def test_outputs_too_high_when_first_guess_is_too_high(self) -> None:
        when(random).randint(0, 100).thenReturn(11)
        when(builtins).input('What number has been chosen?').thenReturn('33', '11')

        self.number_guessing_game.guessing_game()

        verify(self.builtins).print('Too high')

    def test_outputs_too_low_when_first_guess_is_too_low(self) -> None:
        when(random).randint(0, 100).thenReturn(11)
        when(builtins).input('What number has been chosen?').thenReturn('3', '11')

        self.number_guessing_game.guessing_game()

        verify(self.builtins).print('Too low')

    def test_outputs_just_right_when_guess_is_right(self) -> None:
        when(random).randint(0, 100).thenReturn(11)
        when(builtins).input('What number has been chosen?').thenReturn('11')

        self.number_guessing_game.guessing_game()

        verify(self.builtins).print('Just right')

    def test_program_keeps_asking_input_until_guess_is_right(self) -> None:
        when(random).randint(0, 100).thenReturn(22)
        when(builtins).input('What number has been chosen?').thenReturn('11', '33', '38', '44', '22')

        self.number_guessing_game.guessing_game()

        verify(self.builtins, times=5).input('What number has been chosen?')


if __name__ == '__main__':
    unittest.main()
