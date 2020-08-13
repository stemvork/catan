import random

kleuren = ["♠", "♥", "♦", "♣"]
aantallen = ["A", 10, "K", "Q", "J", 9, 8, 7]
deck = [(k, a) for k in kleuren for a in aantallen]
random.shuffle(deck)

spelers = [[deck.pop() for i in range(8)] for i in range(4)]
# A B A' B'
# A: 0 2 
# B: 1 3 

troefkleur = random.choice(kleuren)
rid = 0 # ronde id
sid = 0 # slag id

gewonnenA = []
gewonnenB = []

def trek_willekeurig(lijst):
    _id = random.randrange(8)
    return lijst.pop(_id)

def trek_kleur(lijst, kaart):
    for i, _kaart in enumerate(lijst):
        _kleur = _kaart[0]
        if _kleur is kaart[0]:
            return lijst.pop(i)
    return trek_willekeurig(lijst)


# een slag spelen
slagkaarten = []
slagkaarten.append(trek_willekeurig(spelers[0]))
slagkaarten.append(trek_kleur(spelers[1], slagkaarten[0]))
slagkaarten.append(trek_kleur(spelers[2], slagkaarten[0]))
slagkaarten.append(trek_kleur(spelers[3], slagkaarten[0]))

[print("aantal speler", i, "is", len(speler)) for i, speler in
enumerate(spelers)]

print("slagkaarten", slagkaarten)

# TODO: puntentelling na slag
# TODO: handiger weergeven (gesorteerd) kaarten
# TODO: meerdere slagen
# TODO: meerdere rondes
# TODO: GROOT pygame en weergave

# [print("speler", i, "\n", speler) for i, speler in enumerate(spelers)]
