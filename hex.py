from lib import *

# W = math.sqrt(3) * size
# H = 2 * size
# X = W
# Y = H * 3/4


def hex_corner(center, size, i, flat=False):
    if flat:
        angle_deg = 60 * i
    else:   
        angle_deg = 60 * i - 30

    angle_rad = math.pi / 180 * angle_deg
    return (center[0] + size * math.cos(angle_rad),
            center[1] + size * math.sin(angle_rad))


def draw_hex(screen, center, size, flat=False):
    _pts = [hex_corner(center, size, i) for i in range(6)]
    pygame.draw.polygon(screen, COLOURS[0], _pts)

