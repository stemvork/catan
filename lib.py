import pygame 
import sys
import random
import math


# Needed to initialise e.g. font module
pygame.init()


# Some constants
SCREENDIM   = (400, 400)      # Test dimensions
DEBUG       = True            # Development vs. production
FPS         = 30              # Frames per second


# Colour definitions in RGB
WHITE       = (255, 255, 255)
BG          = (20, 40, 80)


# Colour definitions, list of HEX values 
COLOURS  =  { "red": "#ff0000"
            , "green": "#00ff00"
            , "blue": "#0000ff"
            , "yellow": "#ffff00"
            , "magenta": "#ff00ff"
            , "cyan": "#00ffff"
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
pygame.display.set_caption("Kolonisten v0.1")
clock = pygame.time.Clock()


# Needed for some systems to quit without errors
def proper_exit():
    pygame.quit()
    sys.exit()
