from lib import *

def initial_state():
        return  { "turn": 0
                , "players": 4
                , "scores": [2, 2, 2, 2]
                , "colors": ["red", "white", "blue", "orange"]
                }

STATE = initial_state()
def get_info_height(screen):
    return screen.get_rect().height - 20


def draw_turn(screen):
    turn_txt = res_fnt_3.render("Turn: "+str(STATE["turn"]), True, BLACK)
    turn_rct = turn_txt.get_rect(center=(38,
        get_info_height(screen)+RESSIZE//2+1))
    screen.blit(turn_txt, turn_rct)

def draw_playing(screen):
    _p = STATE["turn"] % 4
    _c = STATE["colors"]
    _pc = COLOURS[_c[_p]]
    pygame.draw.rect(screen, BLACK, (0, get_info_height(screen)-5, 75, 35))
    pygame.draw.rect(screen, _pc, (1, get_info_height(screen)-4, 73, 33))
