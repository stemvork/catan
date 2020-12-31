import wasabi2d as w
from defs import *
from fields import *

def adjust_sprite(sprite, scale):
    try:
        sprite.width = sprite.radius
        sprite.height = sprite.radius
    except:
        pass
    sprite.scale = scale
    x, y = sprite.pos
    x, y = scale*x, scale*y
    sprite.pos = x+scale*sprite.width/2, y+scale*sprite.height/2

def adjust(sprites, scale):
    if isinstance(sprites, list) or isinstance(sprites, set):
        [adjust_sprite(sprite, scale) for sprite in sprites]
    elif isinstance(sprites, w.Group):
        [adjust_sprite(sprite, scale) for sprite in sprites._objects]
    else:
        adjust_sprite(sprites, scale)

s = w.Scene(width=WIDTH, height=HEIGHT)
s.title = S_TITLE
s.background = S_BACKGROUND

bg = s.layers[0]
paper = bg.add_sprite(BG_IMG, scale=SCALE, pos = (BG_W*SCALE/2, s.height/2))
rpaper = s.layers[-1].add_rect(width=paper.width*SCALE, height=paper.height*SCALE, pos=paper.pos)

b  = s.layers[1]
bounds = w.Group([
    b.add_rect(width=W, height=H, color=C+RECTTRANS, pos=P) 
    for W, H, C, P in BOUNDS])
adjust(bounds, SCALE)

dr  = s.layers[2]

dice_rects = w.Group([
    dr.add_rect(width=DIESET_H, height=DIESET_H, 
        color=H+DICETRANS, pos=(BG_W, DIESET_H*j))
    for j, H in enumerate(HCOLOURS)])
adjust(dice_rects, SCALE)

d = s.layers[3]

f = s.layers[4]

# TODO: Refactor below.
yellow_rects_mask = [(0,0), (1,0), (2,0),
                     (0,1), (1,1), (3,1),
                     (0,2), (2,2), (3,2),
                     (1,3), (2,3), (3,3)]
yellow_rects = w.Group([
    f.add_rect(width=53, height=53, color='#ffff0099', pos=(43+68.5*i, 407+65*j))
    for i, j in yellow_rects_mask])
yellow.rects = yellow_rects

blue_rects_mask = [(1,0), (2,0), (3,0),
                   (0,1), (1,1), (2,1), (3,1),
                   (0,2), (1,2), (2,2), (3,2)]
blue_rects = w.Group([
    f.add_rect(width=54, height=54, color='#0000ff99', pos=(430+69*i, 480+65*j))
    for i, j in blue_rects_mask])
blue.rects = blue_rects

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

t  = s.layers[5]
