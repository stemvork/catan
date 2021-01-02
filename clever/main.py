# DEPENDENCIES and MODULES
from pprint import pprint
import wasabi2d as w
import sys

from scene import * # depends on fields, die and defs

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

def cross(tc, idx): # FIXME: won't work with white
    print(f"Crossing {tc}:{idx}")
    _bounds = fields[tc].rects[idx].bounds
    t.add_rect(width=_bounds.width, height=_bounds.height, color='black',
            pos=(_bounds.x+_bounds.width/2, _bounds.y+_bounds.height/2))

# FIXME: Die can be used indefinitely after using once..
# FIXME: Wrong colour can be used for all but blue.
# TODO: Move used die to silver plate

roll = Dieset
mouseclick = None

dice = roll()
dice_sprites = w.Group(dice.render(d))
adjust(dice_sprites, SCALE)

state = 'select'

def call_play(mouseclick):
    global dice

    f, t = map(region, mouseclick) # map to large regions
    fr, fc, tr, tc = *f, *t

    if fr is not None and tr is not None: # cancel invalid clicks
        dprint("Directed click.")
        if fr == 1 and tr != 1: # from dice to paper
            _tc = COLOURS[tc-3] # readable colour
            idx, success = fields[_tc].play(dice, mouseclick, f, t)
            if success:
                cross(_tc, idx)
    else:
        dprint("Undirected click.")

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
    global mouseclick

    if mouseclick is None:
        mouseclick = pos # first click

    elif isinstance(mouseclick, tuple):
        if isinstance(mouseclick[0], int):
            mouseclick = (mouseclick, pos) # two clicks
            call_play(mouseclick)
            mouseclick = None
w.run()
