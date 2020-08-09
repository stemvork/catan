from lib import *

def draw_weird_convex(screen, center, size=SIZE):
    _pts = [(0, 0), (50, 0), (25, 25), (50, 75), (0, 25)]
    draw_with_outline(screen, center, _pts)

def draw_house(screen, center=get_center(), size=SIZE):
    # Some constants
    _s   = size // 8
    hy   = round(_s * 4/5)
    hw   = round(_s * 7/8)
    ht   = round(_s * 9/4)
    htt  = round(_s * 11/4)
    center = center[0] - _s, center[1] + _s 


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

def draw_bar(screen, center, i, size=SIZE):
    # Some constants
    _s   = size // 8
    hy   = round(_s * 4/5)
    hw   = round(_s * 18/8)


    # Bar
    _pts = [ (hw, hy)
           , (-hw, hy)
           , (-hw, -hy)
           , (hw, -hy)
           , (hw, hy)
           ]
    _pts = [rotate_point(p, 90 + 60*i) for p in _pts]
    draw_with_outline(screen, _pts, center)


def draw_church(screen, center, size=SIZE):
    # Some constants
    _s   = size // 7
    hy   = round(_s * 4/5)
    dy   = _s // 2
    hw   = round(_s * 10/8)
    hx   = round(_s * 5/4)
    ht   = round(_s * 7/4)
    hs   = round(_s * 4/4)


    # One line version
    _pts = [ (hw, hy)
           , (-hw, hy)
           , (-hw, -hy-ht+hs)
           , (-hw+hx//2, -hy-ht)
           , (-hw+hx, -hy-ht+hs)
           , (-hw+hx, -hy)
           , (hw, -hy)
           , (hw, hy)
           ]
    _pts = [(p[0], p[1]+dy) for p in _pts]
    draw_with_outline(screen, _pts, center)
