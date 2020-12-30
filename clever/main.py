import wasabi2d as w
def dumpobj(args):
    pprint(vars(args))

def pdir(args):
    print(dir(args))
def adjust(sprites, scale):
    if isinstance(sprites, list) or isinstance(sprites, set):
        for sprite in sprites:
            sprite.scale = scale
            x, y = sprite.pos
            x, y = scale*x, scale*y
            sprite.pos = x+scale*sprite.width/2, y+scale*sprite.height/2
    elif isinstance(sprites, w.Group):
        for sprite in sprites._objects:
            sprite.scale = scale
            x, y = sprite.pos
            x, y = scale*x, scale*y
            sprite.pos = x+scale*sprite.width/2, y+scale*sprite.height/2
    else:
        sprites.scale = scale
        x, y = sprites.pos
        x, y = scale*x, scale*y
        sprites.pos = x+scale*sprites.width/2, y+scale*sprites.height/2

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

HEIGHT = 700
SCALE = HEIGHT/1134
WIDTH = round((135+798)*SCALE)
s = w.Scene(width=WIDTH, height=HEIGHT)
s.title = "Ganz Schön Clever!"
s.background = 0.1, 0.1, 0.1

bg = s.layers[0]
paper = bg.add_sprite('paper', scale=SCALE, pos = (798*SCALE/2, s.height/2))
rpaper = s.layers[-1].add_rect(width=paper.width*SCALE, height=paper.height*SCALE, pos=paper.pos)

RECTTRANS = '00'
b  = s.layers[1]
bounds = w.Group([b.add_rect(width=135, height=383, color='#ff0000'+RECTTRANS),
b.add_rect(width=663, height=135, color='#00ff00'+RECTTRANS, pos=(135, 0)),
b.add_rect(width=663, height=123, color='#0000ff'+RECTTRANS, pos=(135, 135)),
b.add_rect(width=663, height=125, color='#ffff00'+RECTTRANS, pos=(135, 258)),
b.add_rect(width=400, height=372, color='#ff00ff'+RECTTRANS, pos=(0, 383)),
b.add_rect(width=398, height=372, color='#00ffff'+RECTTRANS, pos=(400, 383)),
b.add_rect(width=798, height=140, color='#ff6600'+RECTTRANS, pos=(0, 755)),
b.add_rect(width=798, height=115, color='#00ff66'+RECTTRANS, pos=(0, 895)),
b.add_rect(width=798, height=124, color='#6600ff'+RECTTRANS, pos=(0, 1010)),])
# dicerect    = b.add_rect(width=135, height=383, color='#ff000099')
# roundrect   = b.add_rect(width=663, height=135, color='#00ff0099', pos=(135, 0))
# rerollrect  = b.add_rect(width=663, height=123, color='#0000ff99', pos=(135, 135))
# againrect   = b.add_rect(width=663, height=125, color='#ffff0099', pos=(135, 258))
# yellowrect  = b.add_rect(width=400, height=372, color='#ff00ff99', pos=(0, 383))
# bluerect    = b.add_rect(width=398, height=372, color='#00ffff99', pos=(400, 383))
# greenrect   = b.add_rect(width=798, height=140, color='#ff660099', pos=(0, 755))
# orangerect  = b.add_rect(width=798, height=115, color='#00ff6699', pos=(0, 895))
# purplerect  = b.add_rect(width=798, height=124, color='#6600ff99', pos=(0, 1010))
adjust(bounds, SCALE)
d  = s.layers[2]

dice_rects = w.Group([
d.add_rect(width=135, height=135, color='white', pos=(798, 0)),
d.add_rect(width=135, height=135, color='yellow', pos=(798, 135)),
d.add_rect(width=135, height=135, color='blue', pos=(798, 270)),
d.add_rect(width=135, height=135, color='green', pos=(798, 405)),
d.add_rect(width=135, height=135, color='orange', pos=(798, 540)),
d.add_rect(width=135, height=135, color='purple', pos=(798, 675)),])
adjust(dice_rects, SCALE)

f = s.layers[3]
yellow_rects_mask = [(0,0), (1,0), (2,0),
                     (0,1), (1,1), (3,1),
                     (0,2), (2,2), (3,2),
                     (1,3), (2,3), (3,3)]
yellow_rects = w.Group([
    f.add_rect(width=53, height=53, color='#ffff0099', pos=(43+68.5*i, 407+65*j))
    for i, j in yellow_rects_mask])

blue_rects_mask = [(1,0), (2,0), (3,0),
                   (0,1), (1,1), (2,1), (3,1),
                   (0,2), (1,2), (2,2), (3,2)]
blue_rects = w.Group([
    f.add_rect(width=54, height=54, color='#0000ff99', pos=(430+69*i, 480+65*j))
    for i, j in blue_rects_mask])

green_rects = w.Group([
    f.add_rect(width=54, height=54, color='#00990099', pos=(102+60.28*i, 799))
    for i in range(11)])

orange_rects = w.Group([
    f.add_rect(width=54, height=54, color='#ff660099', pos=(102+60.28*i, 913))
    for i in range(11)])

purple_rects = w.Group([
    f.add_rect(width=54, height=54, color='#6600ff99', pos=(102+60.28*i, 1027))
    for i in range(11)])
[adjust(g, SCALE) for g in f.objects]

t  = s.layers[4]

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
    global mouseclick

    if mouseclick is None:
        # print("First click", pos)
        mouseclick = pos
    elif isinstance(mouseclick, tuple):
        # print("Second (or third?) click", mouseclick, pos)
        if isinstance(mouseclick[0], int):
            mouseclick = (mouseclick, pos)
            _from, _to = mouseclick
            __from, __to = region(_from), region(_to)
            if __from is not None and __to is not None:
                a, b, c, d = *__from, *__to
                if a == 1 and c != 1:
                    if b > 0:
                        if d-b == 3:
                            print(f"Clicked from {__from}{_from} to {__to}{_to}")
                        else:
                            print("Canceled click.")
                    else:
                        print("Playing white die!")
                else:
                    print("Canceled click.")
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
