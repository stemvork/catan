DEBUG = True

COLOURS = ["white", "yellow", "blue", "green", "orange", "purple"]
HCOLOURS = ['#ffffff', '#ffff00', '#0000ff', '#009900', '#ff6600', '#6600ff']

def dprint(*args):
    print(*args) if DEBUG else None

class Fields():
    def __init__(self, n=11):
        self.fields = [None] * n
        self.reqs   = [None] * n
        self.boni   = [None] * n
        self.scores = [None] * n

    def legal(self, dice):
        return True

    def play(self, dice, pos):
        return False

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
