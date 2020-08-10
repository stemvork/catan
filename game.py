from lib import *
from bld import *


# Base functions
def hex_corner(center, i, size=SIZE, flat=False):
    if flat:
        angle_deg = 60 * i
    else:   
        angle_deg = 60 * i - 30


    angle_rad = math.pi / 180 * angle_deg
    return (center[0] + size * math.cos(angle_rad),
            center[1] + size * math.sin(angle_rad))

def hex_middle(center, i, size=SIZE, flat=False):
    a = hex_corner(center, i, size, flat)
    b = hex_corner(center, i+1, size, flat)

    return (a[0] + b[0]) // 2, (a[1] + b[1]) // 2

def corner_of(screen, n, i):
    return hex_corner(get_tile_center(screen, n), i)

def middle_of(screen, n, i):
    return hex_middle(get_tile_center(screen, n), i)

def ring_list(w=2):
    return [(abs(j) + 2*i, j) 
                for j in range(-w, w+1)
                for i in range(-w, w+1-abs(j))]

def draw_hex(screen, center, color=WHITE, size=SIZE,  
        absolute=False, flat=False):
    # Calculate the center pixel coordinate from grid coordinate
    # Unless the absolute flag is True
    if not absolute:
        center = calculate_center(screen, center)

    # Actually draw the hexes to the screen
    _pts = [hex_corner(center, i, size - INSET) for i in range(6)]
    pygame.draw.polygon(screen, color, _pts)

def draw_big_hex(screen, n=2, size=SIZE):
    hexes = ring_list(n)

    for _h in hexes:
        draw_hex(screen, _h)


# Higher-level or testing functions
def color_test(screen, _cl=COLOURS):
    # _idx = [(0, 0), (2, 0), (4, 0)]
    _idx = ring_list()
    [draw_hex(screen, c, COLOURS[k]) for k, c in zip(COLOURS, _idx)]

def base_map_color_test(screen):
    _cl = [ "ore"
          , "wool"
          , "lumber"
          , "grain"
          , "brick"
          , "wool"
          , "brick"
          , "brick"
          , "lumber"
          , "desert"
          , "lumber"
          , "ore"
          , "lumber"
          , "ore"
          , "grain"
          , "wool"
          , "brick"
          , "grain"
          , "wool"
          ]
    [draw_hex(screen, c, COLOURS[k]) for k, c in zip(_cl, ring_list())]
    
def structs_test(screen):
    [draw_house(screen, hex_corner(get_center(), i))
            for i in range(6)]
    [draw_bar(screen, hex_middle(get_center(), i), i)
            for i in range(6)]
    [draw_bar(screen, hex_middle(get_tile_center(screen, 8), i), i)
            for i in range(1, 6)]
    [draw_church(screen, hex_corner(get_tile_center(screen, 8), i))
            for i in range(2, 6)]

def base_structs(screen):
    draw_house(screen, corner_of(screen, 8, 5))
    draw_house(screen, corner_of(screen, 8, 3), colour=COLOURS["red"])
    draw_house(screen, corner_of(screen, 12, 1), colour=COLOURS["lightblue"])
    draw_house(screen, corner_of(screen, 13, 1), colour=COLOURS["orange"])

    draw_bar(screen, middle_of(screen, 8, 4), 4)
    draw_bar(screen, middle_of(screen, 8, 2), 2, colour=COLOURS["red"])
    draw_bar(screen, middle_of(screen, 16, 5), 5, colour=COLOURS["lightblue"])
    draw_bar(screen, middle_of(screen, 17, 5), 5, colour=COLOURS["orange"])

    draw_house(screen, corner_of(screen, 10, 1))
    draw_house(screen, corner_of(screen, 0, 1), colour=COLOURS["red"])
    draw_house(screen, corner_of(screen, 14, 1), colour=COLOURS["lightblue"])
    draw_house(screen, corner_of(screen, 5, 0), colour=COLOURS["orange"])

    draw_bar(screen, middle_of(screen, 10, 0), 0)
    draw_bar(screen, middle_of(screen, 1, 2), 2, colour=COLOURS["red"])
    draw_bar(screen, middle_of(screen, 15, 3), 3, colour=COLOURS["lightblue"])
    draw_bar(screen, middle_of(screen, 5, 5), 5, colour=COLOURS["orange"])

    _res = [10, 2, 9, 12, 6, 4, 10, 9, 11, -1, 3, 8, 8, 3, 4, 5, 5, 6, 11]
    for i, a in enumerate(_res):
        draw_res(screen, get_tile_center(screen, i), a) if a > 0 else None

def get_tile_center(screen, n):
    coord = ring_list()[n]
    return calculate_center(screen, coord)
