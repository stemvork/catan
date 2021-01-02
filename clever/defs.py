DEBUG = True

HEIGHT = 700
SCALE = HEIGHT/1134
WIDTH = round((135+798)*SCALE)

S_TITLE = "Ganz Schön Clever!"
S_BACKGROUND = 0.1, 0.1, 0.1

BG_IMG = 'paper'
BG_W   = 798

RECTTRANS = '00'
DICETRANS = '11'

COLOURS = ["white", "yellow", "blue", "green", "orange", "purple"]
HCOLOURS = ['#ffffff', '#ffff00', '#0000ff', '#009900', '#ff6600', '#6600ff']

BOUNDS = [(135, 383, '#ff0000', (0,0)),
          (663, 135, '#00ff00', (135,0)),
          (663, 123, '#0000ff', (135,135)),
          (663, 125, '#ffff00', (135,258)),
          (400, 372, '#ff00ff', (0, 383)),
          (398, 372, '#00ffff', (400, 383)),
          (798, 140, '#ff6600', (0, 755)),
          (798, 115, '#00ff66', (0, 895)),
          (798, 124, '#6600ff', (0, 1010)),]

def dprint(*args):
    print(*args) if DEBUG else None

class Fields():
    def __init__(self, n=11, **kwargs):
        self.fields = [None] * n
        self.reqs   = [None] * n
        self.boni   = [None] * n
        self.scores = [None] * n

        for key in kwargs:
            self.__dict__[key] = kwargs[key]

    def play(self, dice, mouseclick, f, t):
        fpos, tpos = mouseclick
        fr, fc, tr, tc = *f, *t
        die = dice.select(fc)

        idx, legal = self.legal(die, tpos)

        if legal:
            self.fields[idx] = die.value
            self.reqs[idx]   = None
            return idx, True
        else:
            return idx, False

    def legal(self, die, pos):
        idx = [_.bounds.collidepoint(pos) 
                for _ in self.rects].index(True)
        legal = self.fields[idx] is None
        return idx, True
        return True

    def bonus(self):
        return None

    def score(self):
        return "Total Score"

    def __str__(self):
        return str([(fieldidx, fieldvalue)
            for fieldidx, fieldvalue in enumerate(self.fields)
            if fieldvalue is not None])

    def __repr__(self):
        self.__str__()

DIESET_X = 835
DIESET_Y = 43
DIESET_H = 135

DIE_R_W = 52

YELLOW_REQS = [3, 6, 5, 2, 1,
               5, 1, 2, 4, 3,
               4, 6]
BLUE_REQS   = list(range(2, 13))
GREEN_REQS   = list(range(1, 6)) + list(range(1, 7))
