import wasabi2d as w
def dumpobj(args):
    pprint(vars(args))

def adjust(sprites, scale):
    if isinstance(sprites, list) or isinstance(sprites, set):
        for sprite in sprites:
            sprite.scale = scale
            x, y = sprite.pos
            x, y = scale*x, scale*y
            sprite.pos = x+scale*sprite.width/2, y+scale*sprite.height/2
    else:
        sprites.scale = scale
        sprites.pos = scale*sprites.width/2, scale*sprites.height/2

from pprint import pprint
from die import *
from fields import *

roll = Dieset

# TODO: Develop yellow fields

HEIGHT = 700
SCALE = HEIGHT/1134
WIDTH = round(798*SCALE)
s = w.Scene(width=WIDTH, height=HEIGHT)
s.title = "Ganz Schön Clever!"
s.background = 0.1, 0.1, 0.1

bg = s.layers[0]
paper = bg.add_sprite('paper', scale=SCALE, pos = (798*SCALE/2, s.height/2))

b  = s.layers[1]
dicerect    = b.add_rect(width=135, height=383, color='#ff000099')
roundrect   = b.add_rect(width=663, height=135, color='#00ff0099', pos=(135, 0))
rerollrect  = b.add_rect(width=663, height=123, color='#0000ff99', pos=(135, 135))
againrect   = b.add_rect(width=663, height=125, color='#ffff0099', pos=(135, 258))
yellowrect  = b.add_rect(width=400, height=372, color='#ff00ff99', pos=(0, 383))
bluerect    = b.add_rect(width=398, height=372, color='#00ffff99', pos=(400, 383))
greenrect   = b.add_rect(width=798, height=140, color='#ff660099', pos=(0, 755))
orangerect  = b.add_rect(width=798, height=115, color='#00ff6699', pos=(0, 895))
purplerect  = b.add_rect(width=798, height=124, color='#6600ff99', pos=(0, 1010))
adjust(b.objects, SCALE)

t  = s.layers[2]

# state = 'roll'

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

# @w.event
def on_key_down(key):
    global state, fieldobjs, diceset

    if state == 'roll':
        diceset  = roll()
        state = 'select'

    if state == 'select':
        if key in range(w.keys.K_1, w.keys.K_7):
            dieidx = key - w.keys.K_1
            die = dice[dieidx]
            fieldsobj = fieldsobjs[dieidx]
            die, state, fieldsobj = play(die, state, fieldsobj)
        elif key == w.keys.K_1:
            dieidx = key - w.keys.K_1
            die = dice[dieidx]
            fieldsobj = fieldsobjs[3]
            die, state, fieldsobj = play(die, state, fieldsobj)

    print("FieldsObjs", [_.fields for _ in fieldsobjs if _ is not None])
    print("State", state)
    print()

w.run()
