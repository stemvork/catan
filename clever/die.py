from defs import *
from itertools import chain
import random

class Dieset:
    def __init__(self, colors=[]):
        if len(colors) == 0:
            self.roll()
        else:
            self.dice = [Die(color) for color in colors]

        dprint("Rolled", self.dice)

    def select(self, color):
        if isinstance(color, int):
            offidx = 0 # FIXME: legacy
            if color in range(offidx, offidx+6):
                return self.dice[color-offidx]

        elif isinstance(color, str):
            for die in self.dice:
                if die.color == color:
                    return die

        return None

    def roll(self):
        self.dice = [Die(color) for color in COLOURS]

    def render(self, layer):
        return chain.from_iterable([
            die.render(layer, (DIESET_X, DIESET_Y+DIESET_H*j))
            for j, die in enumerate(self.dice)])

class Die:
    def __init__(self, color):
        self.color = color
        self.roll()

        # render settings
        self.s = DIE_R_W
        self.c, self.tr, self.dr, self.r =\
            self.s/2-2, self.s/4, self.s/6, self.s/12

    def roll(self):
        self.value = random.randint(1, 6)

    def dot(self, pos):
        self.sprites += [self.layer.add_circle(color='black',
            radius=self.r, pos=pos)]
    
    def dots1(self):
        pos = self.x+self.c, self.y+self.c
        self.dot(pos)

    def dots2(self):
        poss = [(self.x+self.c+self.dr, self.y+self.c-self.dr),
                (self.x+self.c-self.dr, self.y+self.c+self.dr),]
        [self.dot(pos) for pos in poss]
    
    def dots3(self):
        poss = [(self.x+self.c+self.tr, self.y+self.c+self.tr),
                (self.x+self.c, self.y+self.c),
                (self.x+self.c-self.tr, self.y+self.c-self.tr),]
        [self.dot(pos) for pos in poss]

    def dots4(self):
        poss = [(self.x+self.c+self.dr, self.y+self.c+self.dr),
                (self.x+self.c+self.dr, self.y+self.c-self.dr),
                (self.x+self.c-self.dr, self.y+self.c+self.dr),
                (self.x+self.c-self.dr, self.y+self.c-self.dr),]
        [self.dot(pos) for pos in poss]

    def dots5(self):
        poss = [(self.x+self.c+self.tr, self.y+self.c+self.tr),
                (self.x+self.c+self.tr, self.y+self.c-self.tr),
                (self.x+self.c, self.y+self.c),
                (self.x+self.c-self.tr, self.y+self.c+self.tr),
                (self.x+self.c-self.tr, self.y+self.c-self.tr),]
        [self.dot(pos) for pos in poss]

    def dots6(self):
        poss = [(self.x+self.c+self.tr, self.y+self.c+self.dr),
                (self.x+self.c+self.tr, self.y+self.c-self.dr),
                (self.x+self.c, self.y+self.c-self.dr),
                (self.x+self.c, self.y+self.c+self.dr),
                (self.x+self.c-self.tr, self.y+self.c+self.dr),
                (self.x+self.c-self.tr, self.y+self.c-self.dr),]
        [self.dot(pos) for pos in poss]
    
    def dots(self):
        if self.value == 1: self.dots1()
        if self.value == 2: self.dots2()
        if self.value == 3: self.dots3()
        if self.value == 4: self.dots4()
        if self.value == 5: self.dots5()
        if self.value == 6: self.dots6()

    def render(self, layer, pos=(0,0)):
        self.layer = layer
        self.x, self.y = pos 

        # coloured small-ish die
        self.sprites = [self.layer.add_rect(
                    width=self.s, height=self.s, pos=pos,
                    color=HCOLOURS[COLOURS.index(self.color)])]

        self.dots()
        return self.sprites

    def __str__(self):
        return self.color + " " + str(self.value)

    def __repr__(self):
        return self.color + " " + str(self.value)


