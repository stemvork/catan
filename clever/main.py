import wasabi2d as w
import random
from pprint import pprint

def dumpobj(args):
    pprint(vars(args))

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

class GreenFields():
    fields = [None] * 11
    reqs   = list(range(1,6)) + list(range(1, 7))
    boni   = [None, None, None, "again", None,
              "xblue", "fuchs", None, "6purple", "reroll",
              None]
    scores = [1, 3, 6, 10, 15,
                          21, 28, 36, 45, 55,
                          66]
    def reset():
        GreenFields.fields = [None] * 11
        GreenFields.reqs   = list(range(1,6)) + list(range(1, 7))
        GreenFields.boni   = [None, None, None, "again", None,
                              "xblue", "fuchs", None, "6purple", "reroll",
                              None]
        GreenFields.scores = [1, 3, 6, 10, 15,
                              21, 28, 36, 45, 55,
                              66]

dice = Die.newset()
dumpobj(GreenFields)


w.run()
