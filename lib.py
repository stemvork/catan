import pygame 
import sys
import random
import math
from itertools import tee
from pygame import gfxdraw as gd


# Needed to initialise e.g. font module
pygame.init()


# Some constants
SCREENDIM   = (400, 400)      # Test dimensions
DEBUG       = True            # Development vs. production
FPS         = 30              # Frames per second
SIZE        = 400 // 9
RESSIZE     = 3*SIZE//9
INSET       = 2


# Colour definitions in RGB
WHITE       = (255, 255, 255)
BLACK       = (0, 0, 0)
BG          = (20, 40, 80)


# Colour definitions, list of HEX values 
COLOURS  =  { "white": "#ffffff"
            , "black": "#000000"
            , "bg" : "#666666"
            , "red": "#ff0000"
            , "green": "#00ff00"
            #, "blue": "#0000ff"
            , "yellow": "#ffff00"
            , "magenta": "#ff00ff"
            , "cyan": "#00ffff"
            , "orange": "#ff9900"
            , "blue": "#0099FF"
            , "sea": "#2d84c9"
            , "desert": "#AF944D"
            , "brick": "#904D14"
            , "ore": "#6A647D"
            , "grain": "#FFC847"
            , "wool": "#98CE00"
            , "lumber": "#3C5200"
            }

# Convert them to pygame colors (RGB)
COLOURS = {k: pygame.Color(v) for k, v in COLOURS.items()}

# Setup the screen and timing
if DEBUG:
    screen = pygame.display.set_mode(SCREENDIM)
else:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Kolonisten v0.3")
clock = pygame.time.Clock()

# Setup some font
res_fnt_1 = pygame.font.SysFont("Arial", RESSIZE//2, True)
res_fnt_2 = pygame.font.SysFont("Arial", 2*RESSIZE//3, True)
res_fnt_3 = pygame.font.SysFont("Arial", RESSIZE, True)


# Needed for some systems to quit without errors
def proper_exit():
    pygame.quit()
    sys.exit()

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def draw_with_outline(screen, pts, center=(0, 0), color=WHITE):
    pts = [(p[0]+center[0], p[1]+center[1]) for p in pts]
    pygame.draw.polygon(screen, color, pts)
    for a, b in pairwise(pts):
        pygame.draw.line(screen, BLACK, a, b)

def get_center():
    return tuple(map(lambda x: x //2, screen.get_rect().size))

def rotate_point(p, a):
    rot_deg = 45
    rot_rad = math.pi / 180 * a
    c = math.cos(rot_rad)
    s = math.sin(rot_rad)
    return p[0] * c - p[1] * s, p[0] * s + p[1] * c

def calculate_center(screen, center, size=SIZE):
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
    return center
