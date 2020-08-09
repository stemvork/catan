from lib import *


# W = math.sqrt(3) * size
# H = 2 * size
# X = W
# Y = H * 3/4


# On axial and cube coords
# The cube coord (x, y, z)
# reads axially  (q, s, r)
# where s is often calculated
# from x + y + z = 0 or
# from s = -q-r


# Fallback size definition
SIZE  = 30
INSET = 3


def hex_corner(center, i, size=SIZE, flat=False):
    if flat:
        angle_deg = 60 * i
    else:   
        angle_deg = 60 * i - 30


    angle_rad = math.pi / 180 * angle_deg
    return (center[0] + size * math.cos(angle_rad),
            center[1] + size * math.sin(angle_rad))


def draw_hex(screen, center, size=SIZE, absolute=False, flat=False):
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
    pygame.draw.polygon(screen, COLOURS[0], _pts)


def ring_list(w):
    return [(abs(j) + 2*i, j) 
                for j in range(-w, w+1)
                for i in range(-w, w+1-abs(j))]

def draw_big_hex(screen, n=2, size=SIZE):
    hexes = ring_list(n)

    for _h in hexes:
        draw_hex(screen, _h)

