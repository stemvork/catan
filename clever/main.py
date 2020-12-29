import wasabi2d as w
from pprint import pprint
from die import *
from fields import *

def dumpobj(args):
    pprint(vars(args))

s = w.Scene()
s.title = "Ganz Schön Clever!"
s.background = 0.1, 0.1, 0.1

b = s.layers[0]
t = s.layers[1]

state = 'roll'
fieldsobjs = [None, YellowFields,
              BlueFields, GreenFields,
              OrangeFields, PurpleFields]

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

def roll():
    return Die.newset()

@w.event
def on_key_down(key):
    global state, GreenFields, dice

    if state == 'roll':
        if key == w.keys.SPACE:
            dice  = roll()
            state = 'select'

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

    print("Dice", dice) if dice else None
    print("FieldsObjs", [_.fields for _ in fieldsobjs if _ is not None])
    print("State", state)
    print()

w.run()
