import wasabi2d as w
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
