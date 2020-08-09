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
    
def base_structs(screen):
    [draw_house(screen, hex_corner(get_center(), i))
            for i in range(6)]
    [draw_bar(screen, hex_middle(get_center(), i), i)
            for i in range(6)]
    [draw_bar(screen, hex_middle(get_tile_center(screen, 8), i), i)
            for i in range(1, 6)]
    [draw_church(screen, hex_corner(get_tile_center(screen, 8), i))
            for i in range(2, 6)]


def get_tile_center(screen, n):
    coord = ring_list()[n]
    return calculate_center(screen, coord)
