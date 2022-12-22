# Implement a class called Game with the following:


# A constructor that takes no arguments and sets an instance variable called score to an initial value of 0.
# A getter method named score that returns the value of a private instance property called _score.
# A setter method named score that sets the value of the private property _score. This method should take a single argument for the value and set _score to this value * 10.

class Game:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value * 10

my_game = Game()
print(my_game.score) # 0

my_game.score = 5
print(my_game.score) # 50