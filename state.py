from lib import *

# GAME STATE AND SETTINGS
game = DotDict({})

game.debug = True

# The screen width and height are the maximum possible width and height.
screensize = (960, 600)
maxwidth, maxheight = screensize

# The following are not necessarily game state
# but in case of trouble with scope, these can
# be accessed through the game state as well.
game.maxwidth = maxwidth
game.maxheight = maxheight
game.screen = pygame.display.set_mode(screensize)
game.center = game.screen.get_rect().center

pygame.display.set_caption("Klaverjassen v0.2")
game.clock  = pygame.time.Clock()
game.colors = colors

spelers, troefkleur = nieuwe_slag()
game.spelers = spelers
game.troefkleur = troefkleur

game.kleuren = kleuren
game.aantallen = aantallen
game.hoogstescores = hoogstescores
game.troefscores = troefscores
game.kaarten = kaarten
game.teams = teams
game.volgorde = volgorde
game.scoreA = 0
game.scoreB = 0
game.sid = 0
game.rid = 0
game.kaartsize = (90, 140)
game.slagkaarten = [None] * 4
game.model = game.troefscores

