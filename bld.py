from lib import *

def draw_weird_convex(screen, center, size=SIZE):
    _pts = [(0, 0), (50, 0), (25, 25), (50, 75), (0, 25)]
    draw_with_outline(screen, center, _pts)

def draw_house(screen, center=list(map(lambda x: x // 2,
        screen.get_rect().size)), size=SIZE):


    # Some constants
    _s   = SIZE // 4
    hy   = round(_s * 4/5)
    hw   = round(_s * 7/8)
    ht   = round(_s * 9/4)
    htt  = round(_s * 11/4)


    # Front face
    _pts = [ (hw, hy)
           , (-hw, hy)
           , (-hw, -hy)
           , (hw, -hy)
           , (hw, hy)
           ]
    draw_with_outline(screen, _pts, center)


    # Triangle
    _pts = [ (-hw, -hy)
           , (hw, -hy)
           , (0, -ht)
           , (-hw, -hy)
           ]
    draw_with_outline(screen, _pts, center)


    # Side roof
    _pts = [ (hw, -hy)
           , (3 * hw, -2 * hy)
           , (2 * hw, -htt)
           , (0, -ht)
           , (hw, -hy)
           ]
    draw_with_outline(screen, _pts, center)


    # Side house
    _pts = [ (hw, hy)
           , (3 * hw, 0)
           , (3 * hw, -2 * hy)
           , (hw, -hy)
           , (hw, hy)
           ]
    draw_with_outline(screen, _pts, center)


