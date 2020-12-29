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

    def __str__(self):
        return self.color + " " + str(self.value)

    def __repr__(self):
        return self.color + " " + str(self.value)

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

    def playnext(die):
        print('playing', die)
        if die.color == 'green':
            next_index = GreenFields.fields.index(None)
            print('next_index', next_index)
            if next_index is None:
                raise Exception('Green is full.')
            else:
                if die.value >= GreenFields.reqs[next_index]:
                    GreenFields.fields[next_index] = die
                    print(GreenFields.fields)
                    # activate boni
                    # update score
                else:
                    raise Exception('Value too low:', die.value, 'for',
                                    GreenFields.reqs[next_index])
        else:
            raise Exception('Die is not green.')

dice = Die.newset()
GreenFields.playnext(dice[3])
GreenFields.playnext(dice[3])
GreenFields.playnext(dice[3])

w.run()
