import sys
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

@w.event
def on_key_down(key):
    if key == w.keys.SPACE:
        dice.roll()
    if key == w.keys.Q:
        sys.exit()

@w.event
def on_mouse_down(pos):
    global mouseclick, dice

    if mouseclick is None:
        mouseclick = pos # first click

    elif isinstance(mouseclick, tuple):
        if isinstance(mouseclick[0], int):
            mouseclick = (mouseclick, pos) # two clicks
            _from, _to = map(region, mouseclick)
            if _from is not None and _to is not None:
                fr, fc, tr, tc = *_from, *_to
                if fr == 1 and tr != 1:
                    if fc > 0:
                        if tc - fc == 3:
                            die = dice.select(fc)
                            fields[die.color].play(die)
                            print(f"Clicked from {_from} to {_to}")
                            print(f"Selected die {die}")
                    else:
                        # field obj: fields[COLOURS[tc-3]]
                        print("Playing white die!")
            mouseclick = None
w.run()
