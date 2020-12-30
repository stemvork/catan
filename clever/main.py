import wasabi2d as w
def dumpobj(args):
    pprint(vars(args))

def pdir(args):
    print(dir(args))

def region(pos):
    if rpaper.bounds.collidepoint(pos):
        for i, rect in enumerate(bounds):
            if rect.bounds.collidepoint(pos):
                return (0, i)
    else:
        for i, die in enumerate(dice_rects):
            if die.bounds.collidepoint(pos):
                return (1, i)

from pprint import pprint
from die import *
from fields import *

roll = Dieset
mouseclick = None

# TODO: Develop yellow fields
# TODO: Indicate actual die value

from scene import *

dice = roll()
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

@w.event
def on_key_down(key):
    if key == w.keys.SPACE:
        dice.roll()
#     global state, fieldobjs, diceset
#
#     if state == 'roll':
#         diceset  = roll()
#         state = 'select'
#
#     if state == 'select':
#         if key in range(w.keys.K_1, w.keys.K_7):
#             dieidx = key - w.keys.K_1
#             die = dice[dieidx]
#             fieldsobj = fieldsobjs[dieidx]
#             die, state, fieldsobj = play(die, state, fieldsobj)
#         elif key == w.keys.K_1:
#             dieidx = key - w.keys.K_1
#             die = dice[dieidx]
#             fieldsobj = fieldsobjs[3]
#             die, state, fieldsobj = play(die, state, fieldsobj)
#
#     print("FieldsObjs", [_.fields for _ in fieldsobjs if _ is not None])
#     print("State", state)
#     print()
@w.event
def on_mouse_down(pos):
    global mouseclick, dice

    if mouseclick is None:
        mouseclick = pos
    elif isinstance(mouseclick, tuple):
        if isinstance(mouseclick[0], int):
            mouseclick = (mouseclick, pos)
            _from, _to = mouseclick
            __from, __to = region(_from), region(_to)
            if __from is not None and __to is not None:
                a, b, c, d = *__from, *__to
                if a == 1 and c != 1:
                    if b > 0:
                        if d-b == 3:
                            die = dice.select(b)
                            fields[die.color].play(die)
                            print(f"Clicked from {__from}{_from} to {__to}{_to}")
                            print(f"Selected die {die}")
                    else:
                        print("Playing white die!")
            mouseclick = None
#         for i, rect in enumerate(dice_rects):
#             if rect.bounds.collidepoint(pos):
#                 die = dice.select(i)
#                 if die:
#                     if die.color == "white":
#                         print("Clicked white!", die)
#                     if die.color == "yellow":
#                         print("Clicked yellow!", die)
#                         fields[die.color].play(die)
#                     if die.color == "blue":
#                         print("Clicked blue!", die)
#                     if die.color == "green":
#                         print("Clicked green!", die)
#                     if die.color == "orange":
#                         print("Clicked orange!", die)
#                     if die.color == "purple":
#                         print("Clicked purple!", die)

w.run()
