from lib import *

def draw_weird_convex(screen, center, size=SIZE, colour=WHITE):
    _pts = [(0, 0), (50, 0), (25, 25), (50, 75), (0, 25)]
    draw_with_outline(screen, center, _pts)

def draw_house(screen, center=get_center(), size=SIZE, colour=WHITE):
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
    draw_with_outline(screen, _pts, center, colour)


    # Triangle
    _pts = [ (-hw, -hy)
           , (hw, -hy)
           , (0, -ht)
           , (-hw, -hy)
           ]
    draw_with_outline(screen, _pts, center, colour)


    # Side roof
    _pts = [ (hw, -hy)
           , (3 * hw, -2 * hy)
           , (2 * hw, -htt)
           , (0, -ht)
           , (hw, -hy)
           ]
    draw_with_outline(screen, _pts, center, colour)


    # Side house
    _pts = [ (hw, hy)
           , (3 * hw, 0)
           , (3 * hw, -2 * hy)
           , (hw, -hy)
           , (hw, hy)
           ]
    draw_with_outline(screen, _pts, center, colour)

def draw_bar(screen, center, i, size=SIZE, colour=WHITE):
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
    draw_with_outline(screen, _pts, center, colour)

def draw_church(screen, center, size=SIZE, colour=WHITE):
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
    draw_with_outline(screen, _pts, center, colour)

def draw_robber(screen, center, size=SIZE):
    _s     = size // 2
    cx, cy = center
    rw     = round(_s * 5/8)
    rh     = round(_s * 9/8)
    rhw    = round(_s * 4/8)
    rhh    = round(_s * 4/8)
    rbh    = round(_s * 2/8)

    pygame.draw.ellipse(screen, BLACK, (
        cx - rw//2, cy - rh//2, rw, rh))
    pygame.draw.ellipse(screen, BLACK, (
        cx - rhw//2-1, cy - 3*rhh//7 - 3*rh//5, rhw + 1, rhh))
    pygame.draw.rect(screen, BLACK, (
        cx - rw//2, cy + 3*rh//7 - rbh//2, rw, rbh))

def draw_res(screen, center, amount, size=SIZE):
    pygame.draw.circle(screen, COLOURS["desert"], center, RESSIZE)
    [gd.aacircle(screen, *tuple(map(round, center)), RESSIZE, BLACK)
            for c in range(-1, 1)]
    if amount in [2, 3, 12, 11]:
        res_txt = res_fnt_1.render(str(amount), True, BLACK)
    elif amount in [4, 5, 10, 9]:
        res_txt = res_fnt_2.render(str(amount), True, BLACK)
    elif amount in [6, 7, 8]:
        res_txt = res_fnt_3.render(str(amount), True, BLACK)
    res_rct = res_txt.get_rect(center=center)
    screen.blit(res_txt, res_rct)
