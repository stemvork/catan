from die import * # depends on defs

def absorb(inst, func, cls=Fields):
    _func = func.__name__.split('_')[1]
    setattr(inst, _func, func.__get__(inst, cls))

def legal_report(legal, die, pos):
    if legal:
        dprint(f"{die} played to {pos}")
    else:
        dprint(f"ILLEGAL: {die} played to {pos}")


def yellow_legal(self, die, pos):
    idx = self.idx(die, pos)
    legal = self.fields[idx] is None and self.reqs[idx] == die.value
    legal_report(legal, die, pos)
    return idx, legal

def orange_legal(self, die, pos):
    idx = self.idx(die, pos)
    legal = True
    legal_report(legal, die, pos)
    return idx, legal

def blue_legal(self, dice, pos):
    wdie = dice.select("white")
    bdie = dice.select("blue")
    # print(wdie, bdie)
    dsum = wdie.value + bdie.value
    idx = [_.bounds.collidepoint(pos)
            for _ in self.rects].index(True)
    legal = self.fields[idx] is None and self.reqs[idx] == dsum
    legal_report(legal, (wdie, bdie), pos)
    return idx, legal, dsum

def green_legal(self, die, pos):
    print(self, die, pos)
    idx = [_.bounds.collidepoint(pos) 
            for _ in self.rects].index(True)
    legal = self.fields[idx] is None and self.reqs[idx] <= die.value
    legal_report(legal, die, pos)
    return idx, legal

def purple_legal(self, die, pos):
    # FIXME: Fails if not pressing on a subregion
    idx = [_.bounds.collidepoint(pos) 
            for _ in self.rects].index(True)
    if idx > 0:
        prev = self.fields[idx-1]
        if prev == 6:
            legal = True
        else:
            legal = self.fields[idx] is None and prev < die.value
    else:
        legal = True
    legal_report(legal, die, pos)
    return idx, legal


def blue_play(self, dice, mouseclick, f, t):
    fpos, tpos = mouseclick
    fr, fc, tr, tc = *f, *t
    # die = dice.select(fc)

    idx, legal, dsum = self.legal(dice, tpos)

    if legal:
        self.fields[idx] = dsum
        self.reqs[idx]   = None
        return idx, True
    else:
        return idx, False

yellow = Fields(n = 12, reqs = YELLOW_REQS)
absorb(yellow, yellow_legal)

blue = Fields(reqs = BLUE_REQS)
absorb(blue, blue_legal)
absorb(blue, blue_play)

green = Fields(reqs = GREEN_REQS)
absorb(green, green_legal)

orange = Fields()

purple = Fields()
absorb(purple, purple_legal)

fields = {"yellow": yellow,
          "blue": blue,
          "green": green,
          "orange": orange,
          "purple": purple,
         }

