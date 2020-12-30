import random

COLOURS = ["white", "yellow", "blue", "green", "orange", "purple"]
HCOLOURS = ['#ffffff', '#ffff00', '#0000ff', '#009900', '#ff6600', '#6600ff']

class Dieset:
    def __init__(self, colors=[]):
        if len(colors) == 0:
            self.roll()
        else:
            self.dice = [Die(color) for color in colors]
        print("Rolled", self.dice)

    def select(self, color):
        if isinstance(color, int):
            offidx = 0
            if color in range(offidx, offidx+6):
                return self.dice[color-offidx]
        elif isinstance(color, str):
            for die in self.dice:
                if die.color == color:
                    return die
        return None

    def roll(self):
        self.dice = [Die(color) for color in COLOURS]

class Die:
    def __init__(self, color):
        self.color = color
        self.roll()

    def roll(self):
        self.value = random.randint(1, 6)

    # TODO refactor huge die render function
    def render(self, layer, pos=(0,0)):
        x, y = pos
        s    = 54
        c    = s/2-2
        tr   = s/4
        dr   = s/6
        r    = s/12

        sprites = [layer.add_rect(
                    width=s, height=s, pos=pos,
                    color=HCOLOURS[COLOURS.index(self.color)])]
        if self.value == 1:
            sprites += [layer.add_circle(color='black', radius=r,
                                         pos=(x+c, y+c))]
        if self.value == 2:
            sprites += [layer.add_circle(color='black', radius=r,
                                         pos=(x+c+dr, y+c-dr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c-dr, y+c+dr)),]
        if self.value == 3:
            sprites += [layer.add_circle(color='black', radius=r,
                                         pos=(x+c+tr, y+c+tr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c, y+c)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c-tr, y+c-tr)),]
        if self.value == 4:
            sprites += [layer.add_circle(color='black', radius=r,
                                         pos=(x+c+dr, y+c-dr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c+dr, y+c+dr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c-dr, y+c-dr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c-dr, y+c+dr)),]
        if self.value == 5:
            sprites += [layer.add_circle(color='black', radius=r,
                                         pos=(x+c+tr, y+c+tr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c+tr, y+c-tr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c, y+c)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c-tr, y+c-tr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c-tr, y+c+tr)),]
        if self.value == 6:
            sprites += [layer.add_circle(color='black', radius=r,
                                         pos=(x+c+tr, y+c+dr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c+tr, y+c-dr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c, y+c-dr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c, y+c+dr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c-tr, y+c-dr)),
                        layer.add_circle(color='black', radius=r,
                                         pos=(x+c-tr, y+c+dr)),]
        return sprites

    def __str__(self):
        return self.color + " " + str(self.value)

    def __repr__(self):
        return self.color + " " + str(self.value)


