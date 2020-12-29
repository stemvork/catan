import random

class Dieset:
    def __init__(self, colors=[]):
        if len(colors) == 0:
            self.roll()
        else:
            self.dice = [Die(color) for color in colors]
        print("Rolled", self.dice)

    def select(self, color):
        if isinstance(color, int):
            offidx = 0
            if color in range(offidx, offidx+6):
                return self.dice[color-offidx]
        elif isinstance(color, str):
            for die in self.dice:
                if die.color == color:
                    return die
        return None

    def roll(self):
        self.dice = [Die(color) for color in
               ["white", "yellow", "blue", "green", "orange", "purple"]]

class Die:
    def __init__(self, color):
        self.color = color
        self.roll()

    def roll(self):
        self.value = random.randint(1, 6)

    def __str__(self):
        return self.color + " " + str(self.value)

    def __repr__(self):
        return self.color + " " + str(self.value)


