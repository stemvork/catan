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

class YellowFields():
    color  = 'yellow'
    fields = [None] * 12
    reqs   = [3, 6, 5, 2, 1,
              5, 1, 2, 4, 3,
              4, 6]
    # TODO: boni for yellow
    boni   = [None] * 12
    scores = reqs
    def reset():
        YellowFields.fields = [None] * 12
        YellowFields.reqs   = [3, 6, 5, 2, 1,
                               5, 1, 2, 4, 3,
                               4, 6]
        YellowFields.boni   = [None] * 12
        YellowFields.scores = YellowFields.reqs

    def playnext(die):
        if die.color == 'green':
            next_index = YellowFields.fields.index(None)
            if next_index is not None:
                if die.value >= YellowFields.reqs[next_index]:
                    YellowFields.fields[next_index] = die
                    return True
                    # activate boni
                    # update score
class BlueFields():
    color  = 'blue'
    fields = [None] * 11
    reqs   = list(range(2, 13))
    # TODO: boni for blue
    boni   = [None] * 11
    scores = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56]
    def reset():
        BlueFields.fields = [None] * 11
        BlueFields.reqs   = list(range(2, 13))
        BlueFields.boni = [None] * 11
        BlueFields.boni   = [None, None, None, "again", None,
                              "xblue", "fuchs", None, "6purple", "reroll",
                              None]
        BlueFields.scores = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56]

    def playnext(die):
        if die.color == 'green':
            next_index = BlueFields.fields.index(None)
            if next_index is not None:
                if die.value >= BlueFields.reqs[next_index]:
                    BlueFields.fields[next_index] = die
                    return True
                    # activate boni
                    # update score
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
class OrangeFields():
    color  = 'orange'
    fields = [None] * 11
    reqs   = [None] * 11
    boni   = [None, None, "reroll", "double", "xyellow",
              "again", "double", "fuchs", "double", "6purple",
              None]
    scores = [None] * 11
    def reset():
        OrangeFields.fields = [None] * 11
        OrangeFields.reqs   = [None] * 11
        OrangeFields.boni   = [None, None, "reroll", "double", "xyellow",
                               "again", "double", "fuchs", "double", "6purple",
                               None]
        OrangeFields.scores = [None] * 11

    def playnext(die):
        if die.color == 'green':
            next_index = OrangeFields.fields.index(None)
            if next_index is not None:
                if die.value >= OrangeFields.reqs[next_index]:
                    OrangeFields.fields[next_index] = die
                    return True
                    # activate boni
                    # update score
class PurpleFields():
    color  = 'purple'
    fields = [None] * 11
    reqs   = [None] * 11
    # TODO: implement reqs for purple
    boni   = [None, None, "reroll", "xblue", "again",
              "xyellow", "fuchs", "reroll", "xgreen", "6orange",
              "again"]
    scores = [None] * 11
    def reset():
        PurpleFields.fields = [None] * 11
        PurpleFields.reqs   = [None] * 11
        PurpleFields.boni   = [None, None, "reroll", "xblue", "again",
                              "xyellow", "fuchs", "reroll", "xgreen", "6orange",
                              "again"]
        PurpleFields.scores = [None] * 11
    def playnext(die):
        if die.color == 'green':
            next_index = PurpleFields.fields.index(None)
            if next_index is not None:
                if die.value >= PurpleFields.reqs[next_index]:
                    PurpleFields.fields[next_index] = die
                    return True
                    # activate boni
                    # update score

fieldsobjs = [None, YellowFields, BlueFields, GreenFields, OrangeFields,
              PurpleFields]

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
        if key in range(w.keys.K_2, w.keys.K_7): # not white
            dieidx = key - w.keys.K_1
            die = dice[dieidx]
            fieldsobj = fieldsobjs[dieidx]
            die, state, fieldsobj = play(die, state, fieldsobj)
        elif key == w.keys.K_1:
            dieidx = key - w.keys.K_1
            die = dice[dieidx]
            fieldsobj = fieldsobjs[3]
            die, state, fieldsobj = play(die, state, fieldsobj)

    print("Dice", dice)
    print("FieldsObjs", [_.fields for _ in fieldsobjs if _ is not None])
    print("State", state)
    print()
w.run()
