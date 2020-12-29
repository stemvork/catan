import wasabi2d as w
import random
from pprint import pprint

# TODO: abstract play die to fields, show fields if success, die+req if fails
# TODO: refactor keypress function calls

def dumpobj(args):
    pprint(vars(args))

s = w.Scene()
s.title = "Ganz Schön Clever!"
s.background = 0.1, 0.1, 0.1

b = s.layers[0]
t = s.layers[1]

state = 'roll'

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
    color  = 'green'
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
        if die.color == 'green':
            next_index = GreenFields.fields.index(None)
            if next_index is not None:
                if die.value >= GreenFields.reqs[next_index]:
                    GreenFields.fields[next_index] = die
                    return True
                    # activate boni
                    # update score

dice = Die.newset()
state = 'select'

def play(die, state, fieldsobj):
    if fieldsobj.color == die.color:
        try:
            nextidx = fieldsobj.fields.index(None)
        except:
            nextidx = None
        if nextidx is not None:
            if die.value >= fieldsobj.reqs[nextidx]:
                fieldsobj.fields[nextidx] = die
                state = 'roll'
    return die, state, fieldsobj

def roll(dice, state):
    dice = Die.newset()
    return dice, 'select'

@w.event
def on_key_down(key):
    global state, GreenFields, dice

    if state == 'roll':
        if key == w.keys.SPACE:
            dice, state = roll(dice, state)

    if state == 'select':
        if key in range(w.keys.K_1, w.keys.K_7):
            die = dice[key-w.keys.K_1]
            fieldsobj = GreenFields
            die, state, fieldsobj = play(die, state, fieldsobj)

    print("Dice", dice)
    print("GreenFields", GreenFields.fields)
    print("State", state)
    print()
w.run()
