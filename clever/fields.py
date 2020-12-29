from die import *

class Fields():
    def __init__(self, n=11):
        self.fields = [None] * n
        self.reqs   = [None] * n
        self.boni   = [None] * n
        self.scores = [None] * n

    def legal(self, dice):
        return True

    def play(self, dice):
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

class Yellow(Fields):
    def __init__(self):
        super().__init__(12)
        self.reqs = [3, 6, 5, 2, 1,
                     5, 1, 2, 4, 3,
                     4, 6]

    def ids(self, die):
        return [i for i, v in enumerate(self.reqs)
               if v == die.value]

    def legal(self, die):
        print('checking: legal to play yellow')
        return len(self.ids(die)) > 0

    def play(self, die):
        if self.legal(die):
            print('playing die', die)
            return True
        else:
            return False

    def bonus(self):
        super().bonus()

    def score(self):
        super().score()

yellow = Yellow()
yellow.play(Die("yellow"))
print(yellow)

class YellowFields():
    color  = 'yellow'
    fields = [None] * 12
    reqs   = [3, 6, 5, 2, 1,
              5, 1, 2, 4, 3,
              4, 6]
    # TODO: boni for yellow
    boni   = [None] * 12
    scores = reqs
    def reset():
        YellowFields.fields = [None] * 12
        YellowFields.reqs   = [3, 6, 5, 2, 1,
                               5, 1, 2, 4, 3,
                               4, 6]
        YellowFields.boni   = [None] * 12
        YellowFields.scores = YellowFields.reqs

    def playnext(die):
        if die.color == 'yellow':
            nextidcs = YellowFields.reqs.find(die.value)
            print("Yellow", die.value, nextidcs)
#             if next_index is not None:
#                 if die.value >= YellowFields.reqs[next_index]:
#                     YellowFields.fields[next_index] = die
#                     return True
#                     # activate boni
#                     # update score
class BlueFields():
    color  = 'blue'
    fields = [None] * 11
    reqs   = list(range(2, 13))
    # TODO: boni for blue
    boni   = [None] * 11
    scores = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56]
    def reset():
        BlueFields.fields = [None] * 11
        BlueFields.reqs   = list(range(2, 13))
        BlueFields.boni = [None] * 11
        BlueFields.boni   = [None, None, None, "again", None,
                              "xblue", "fuchs", None, "6purple", "reroll",
                              None]
        BlueFields.scores = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56]

    def playnext(die, dice):
        if die.color == 'blue':
            bluedie  = die
            whitedie = dice.select('white')
        elif die.color == 'white':
            whitedie = die
            bluedie  = dice.select('blue')
        diesum = whitedie.value + bluedie.value
        try:
            nextidx = BlueFields.reqs.index(diesum)
        except:
            nextidx = None
        if nextidx is not None:
            BlueFields.fields[nextidx] = die
            return True
            # activate boni
            # update score

class GreenFields():
    color  = 'green'
    fields = [None] * 11
    reqs   = list(range(1,6)) + list(range(1, 7))
    boni   = [None, None, None, "again", None,
              "xblue", "fuchs", None, "6purple", "reroll",
              None]
    scores = [1, 3, 6, 10, 15,
                          21, 28, 36, 45, 55,
                          66]
    def reset():
        GreenFields.fields = [None] * 11
        GreenFields.reqs   = list(range(1,6)) + list(range(1, 7))
        GreenFields.boni   = [None, None, None, "again", None,
                              "xblue", "fuchs", None, "6purple", "reroll",
                              None]
        GreenFields.scores = [1, 3, 6, 10, 15,
                              21, 28, 36, 45, 55,
                              66]

    def playnext(die):
        if die.color == 'green':
            next_index = GreenFields.fields.index(None)
            if next_index is not None:
                if die.value >= GreenFields.reqs[next_index]:
                    GreenFields.fields[next_index] = die
                    return True
                    # activate boni
                    # update score
class OrangeFields():
    color  = 'orange'
    fields = [None] * 11
    reqs   = [None] * 11
    boni   = [None, None, "reroll", "double", "xyellow",
              "again", "double", "fuchs", "double", "6purple",
              None]
    scores = [None] * 11
    def reset():
        OrangeFields.fields = [None] * 11
        OrangeFields.reqs   = [None] * 11
        OrangeFields.boni   = [None, None, "reroll", "double", "xyellow",
                               "again", "double", "fuchs", "double", "6purple",
                               None]
        OrangeFields.scores = [None] * 11

    def playnext(die):
        if die.color == 'orange':
            try:
                nextidx = OrangeFields.fields.index(None)
            except:
                nextidx = None
            if nextidx is not None:
                OrangeFields.fields[nextidx] = die.value
                return True
                # activate boni
                # update score

class PurpleFields():
    color  = 'purple'
    fields = [None] * 11
    reqs   = [None] * 11
    # TODO: implement reqs for purple
    boni   = [None, None, "reroll", "xblue", "again",
              "xyellow", "fuchs", "reroll", "xgreen", "6orange",
              "again"]
    scores = [None] * 11
    def reset():
        PurpleFields.fields = [None] * 11
        PurpleFields.reqs   = [None] * 11
        PurpleFields.boni   = [None, None, "reroll", "xblue", "again",
                              "xyellow", "fuchs", "reroll", "xgreen", "6orange",
                              "again"]
        PurpleFields.scores = [None] * 11
    def playnext(die):
        if die.color == 'purple':
            nextidx = PurpleFields.fields.index(None)
            if die.value == 6:
                PurpleFields.fields[nextidx] = die.value
                return True
            else:
                if PurpleFields.fields[nextidx-1] < die.value:
                    PurpleFields.fields[nextidx] = die.value
                    return True
                    # activate boni
                    # update score

fieldsobjs = [None, YellowFields,
              BlueFields, GreenFields,
              OrangeFields, PurpleFields]

