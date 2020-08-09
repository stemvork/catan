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
BLACK       = (0, 0, 0)
BG          = (20, 40, 80)


# Colour definitions, list of HEX values 
COLOURS = [ "#ff0000"
          , "#00ff00"
          , "#0000ff"
          , "#ffff00"
          , "#ff00ff"
          , "#00ffff"
          ]

# Convert them to pygame colors (RGB)
COLOURS = [pygame.Color(c) for c in COLOURS]

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
