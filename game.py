from lib import *

# All of the relevant assets and requirements are
# imported by importing everything mentioned in lib.

# assets.py defines the fonts and colours.

# dotdict.py allows for convenient dictionary access.
# Note that dictionary access is now colours.red
# rather than colors["red"] (standard dictionary)
# and also not colors[0] (standard list).

# state.py contains the game state object and inital values

#-------- LOGIC FUNCTIONS

# High-level update function,
# keeps track of actions that respond to inputs.

def update(game):
    for event in pygame.event.get():
        handle_quit(event)
        switch_state(event)
        next_troef(game, event)
        speel_slagkaarten(game, event)
        next_score(game, event)

#-------- DRAW FUNCTIONS

# High-level draw function,
# delegates to the specific draw functions.

def draw(game):
    game.screen.fill(colors.bg)
    draw_troef(game.screen, game.troefkleur)
    draw_kaarten(game.screen, game.spelers[0])
    draw_slagkaarten(game.screen, game.slagkaarten)
    draw_scores(game.screen, (game.scoreA, game.scoreB))
    next_frame()

def draw_troef(screen, troefkleur):
    troef_pos = (90, 400)
    _color = als_kleur(troefkleur)
    troef_text_height = symbols.size(troefkleur)[1]
    troef_text = symbols.render(troefkleur, True, _color)
    troef_text_center = troef_pos[0], troef_pos[1] + troef_text_height//10
    troef_rect = troef_text.get_rect(center=(troef_text_center))
    pygame.draw.circle(screen, colors.white, troef_pos, 30)
    screen.blit(troef_text, troef_rect)

def draw_kaarten(screen, speler):
    for i, kaart in enumerate(speler):
        _kaart_img  = pygame.Surface(game.kaartsize)
        _kaart_img.fill(colors.white)
        _kaart_rect = pygame.Rect( 45 + (10 + game.kaartsize[0]) * i
                         , 450, *game.kaartsize)
        _kleur = als_kleur(kaart[0])
        _text_img = symbols_small.render(kaart_plat(kaart), True, _kleur)
        _text_rect = _text_img.get_rect(center=_kaart_img.get_rect().center)
        _kaart_img.blit(_text_img, _text_rect)

        screen.blit(_kaart_img, _kaart_rect)

def draw_slagkaarten(screen, slagkaarten):
    positions = [(100, 150), (200, 60), (300, 150), (200, 240)]
    for i, slagkaart in enumerate(slagkaarten):
        _kaart_img  = pygame.Surface(game.kaartsize)
        _kaart_img.fill(colors.gray)
        _kaart_rect = (*positions[i], *game.kaartsize)
        if slagkaart is not None:
            _kaart_img.fill(colors.white)
            _kleur = als_kleur(slagkaart[0][0])
            _text_img = symbols_small.render(kaart_plat(slagkaart[0]), True, _kleur)
            _text_rect = _text_img.get_rect(center=_kaart_img.get_rect().center)
            _kaart_img.blit(_text_img, _text_rect)
        screen.blit(_kaart_img, _kaart_rect)

def draw_scores(screen, scores):
    infosize = (480, 400)
    _info_img  = pygame.Surface(infosize)
    _info_img.fill(colors.gray)
    _info_rect = (480, 0, *infosize)

    _text_img = symbols_small.render("Wij", True, colors.yellow)
    _text_rect = _text_img.get_rect(topright=(280, 80))
    _info_img.blit(_text_img, _text_rect)

    _text_img = symbols_small.render("Zij", True, colors.yellow)
    _text_rect = _text_img.get_rect(topright=(390, 80))
    _info_img.blit(_text_img, _text_rect)

    _text_img = symbols_small.render("Totaal", True, colors.yellow)
    _text_rect = _text_img.get_rect(topleft=(90, 200))
    _info_img.blit(_text_img, _text_rect)

    _text_img = symbols_small.render(str(scores[0]), True, colors.yellow)
    _text_rect = _text_img.get_rect(topright=(280, 200))
    _info_img.blit(_text_img, _text_rect)

    _text_img = symbols_small.render(str(scores[1]), True, colors.yellow)
    _text_rect = _text_img.get_rect(topright=(390, 200))
    _info_img.blit(_text_img, _text_rect)

    screen.blit(_info_img, _info_rect)


# Draws a text-wrapped list of strings to the screen
def draw_multi_line(maxwidth, lines, 
        font=written, color=colors.white, padding=0, center=True):

    linesurfaces = [font.render(line, True, color) for line in lines]
    totalheight = sum([surface.get_size()[1] for surface in linesurfaces])

    textsurface = pygame.Surface((maxwidth, totalheight))
    textsurface.set_colorkey(colors.black)
    textsurface_center = textsurface.get_rect().center

    next_height = 0
    for line in linesurfaces:
        if center:
            line_position = textsurface_center[0], next_height
            textsurface.blit(line, line.get_rect(midtop=line_position))
        else:
            textsurface.blit(line, line.get_rect(top=next_height))
        next_height += line.get_rect().height + padding
    return textsurface

# Draw a string to the screen that fits the screen without wrapping
def draw_single_line(maxwidth, text, 
        font=written, color=colors.white, center=True):

    lineheight = font.size(text)[1]

    textsurface = pygame.Surface((maxwidth, lineheight))
    textsurface.set_colorkey(colors.black)
    textsurface_center = textsurface.get_rect().center
    
    line_img  = font.render(text, True, color)

    if center:
        line_rect = line_img.get_rect(center = textsurface_center)
    else:
        line_rect = line_img.get_rect()

    textsurface.blit(line_img, line_rect)
    return textsurface

# Shortcut to display the buffer and await next game loop
def next_frame():
    pygame.display.flip()
    game.clock.tick(30)

#------- EVENT HANDLERS

# These are called from the update function
# and respond to user input by updating the game
# state object accordingly.

# Allows to exit using Esc, q and the OS-default way
def handle_quit(event):
    if event.type == pygame.QUIT:
        proper_exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            proper_exit()
        elif event.key == pygame.K_q:
            proper_exit()

# Switch to the next mode with `m` (debugging)
def switch_state(event):
    if event.type == pygame.KEYDOWN:
        if event.key is pygame.K_m:
            game.states.append(game.states.pop(0))
            game.state = game.states[0]

def next_troef(game, event):
    if event.type == pygame.KEYDOWN:
        if event.key is pygame.K_SPACE:
            game.troefkleur = random.choice(kleuren)

def speel_slagkaarten(game, event):
    if event.type == pygame.KEYDOWN:
        if event.key is pygame.K_a:
           speel_slag(game) 

def next_score(game, event):
    if event.type == pygame.KEYDOWN:
        if event.key is pygame.K_s:
           _scoreA, _scoreB = scoor(game) 
           game.scoreA += _scoreA
           game.scoreB += _scoreB
           game.slagkaarten = [None] * 4

