from lib import *


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

def ring_list(w):
    return [(abs(j) + 2*i, j) 
                for j in range(-w, w+1)
                for i in range(-w, w+1-abs(j))]
def draw_hex(screen, center, color=WHITE, size=SIZE,  
        absolute=False, flat=False):
    # Calculate the center pixel coordinate from grid coordinate
    # Unless the absolute flag is True
    if not absolute:


        # Calculate some derived dimensions
        _w = math.sqrt(3) * size
        _h = 2 * size
        _x = _w
        _y = _h * 3 // 4


        # Draw odd rows with offset to the right
        center = (_x * center[0] // 2 \
                      + screen.get_rect().width // 2, 
                  _y * center[1]\
                      + screen.get_rect().height // 2)


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
    _idx = ring_list(2)
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
    [draw_hex(screen, c, COLOURS[k]) for k, c in zip(_cl, ring_list(2))]
    

