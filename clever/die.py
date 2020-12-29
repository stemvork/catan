import random

class Die:
    def __init__(self, color):
        self.color = color
        self.roll()

    def roll(self):
        self.value = random.randint(1, 6)
        print("Rolled a", self.color, self.value)

    def newset():
        return [Die(color)
            for color in
            ["white", "yellow", "blue", "green", "orange", "purple"]]

    def __str__(self):
        return self.color + " " + str(self.value)

    def __repr__(self):
        return self.color + " " + str(self.value)


