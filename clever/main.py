import wasabi2d as w
import random

s = w.Scene()
s.title = "Ganz Schön Clever!"
s.background = 0.1, 0.1, 0.1

b = s.layers[0]
t = s.layers[1]

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

dice = Die.newset()

w.run()
