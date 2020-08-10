from lib import *

def initial_state():
        return  { "turn": 0
                , "players": 4
                , "scores": [2, 2, 2, 2]
                , "colors": ["red", "white", "blue", "orange"]
                }
STATE = initial_state()


def draw_turn(screen):
    turn_txt = res_fnt_3.render("Turn: "+str(STATE["turn"]), True, BLACK)
    turn_rct = turn_txt.get_rect(center=(
            3 * RESSIZE, screen.get_rect().height - RESSIZE))
    screen.blit(turn_txt, turn_rct)

def draw_playing(screen):
    _p = STATE["turn"] % 4
    _c = STATE["colors"]
    _pc = COLOURS[_c[_p]]
    pygame.draw.rect(screen, BLACK, (0, screen.get_rect().height - 2 * RESSIZE,
        6 * RESSIZE, 2 * RESSIZE))
    pygame.draw.rect(screen, _pc, (1, screen.get_rect().height - 2 * RESSIZE + 1,
        6 * RESSIZE - 2, 2 * RESSIZE - 2))
