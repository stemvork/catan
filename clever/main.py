# DEPENDENCIES and MODULES
from pprint import pprint
import wasabi2d as w
import sys

from die import *
# from fields import *
from scene import *

# AUX FUNCTIONS
def clear_layer(layer):
    for obj in reversed(list(layer.objects)):
        obj.delete()

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

def cross(die, idx):
    _bounds = fields[die.color].rects[idx].bounds
    t.add_rect(width=_bounds.width, height=_bounds.height, color='black',
            pos=(_bounds.x+_bounds.width/2, _bounds.y+_bounds.height/2))

# TODO: Develop yellow fields
# TODO: Move used die to silver plate
# TODO: Refactor

roll = Dieset
mouseclick = None

dice = roll()
dice_sprites = w.Group(dice.render(d))
adjust(dice_sprites, SCALE)

state = 'select'

@w.event
def on_key_down(key):
    if key == w.keys.SPACE:
        clear_layer(d)
        dice.roll()
        dice_sprites = w.Group(dice.render(d))
        adjust(dice_sprites, SCALE)
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
                            idx, success = fields[die.color].play(die, mouseclick[1])
                            if success:
                                cross(die, idx)
                    else:
                        # field obj: fields[COLOURS[tc-3]]
                        print("Playing white die!")
            mouseclick = None
w.run()
