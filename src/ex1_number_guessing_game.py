import builtins
import random


class NumberGuessingGame:
    def __init__(self, random, builtins):
        self.random = random
        self.builtins = builtins

    def guessing_game(self):
        number = self.random.randint(0, 100)

        while True:
            guess = int(self.builtins.input('What number has been chosen?'))

            if guess == number:
                self.builtins.print('Just right')
                break
            elif guess > number:
                self.builtins.print('Too high')
            else:
                self.builtins.print('Too low')


number_guessing_game = NumberGuessingGame(random=random, builtins=builtins)
number_guessing_game.guessing_game()
