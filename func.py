from lib import *

def nieuwe_slag():
    deck = nieuw_deck() # deck is na uitdelen leeg
    spelers = nieuwe_hand(deck)
    troefkleur = random.choice(kleuren)
    return spelers, troefkleur

def nieuw_deck():
    kleuren = ["♠", "♥", "♦", "♣"]
    aantallen = ["A", 10, "K", "Q", "J", 9, 8, 7]
    deck = [(k, a) for k in kleuren for a in aantallen]
    random.shuffle(deck)
    return deck

def nieuwe_hand(deck):
    spelers = [[deck.pop() for i in range(8)] for i in range(4)]
    return spelers

def trek_willekeurig(lijst):
    _id = random.randrange(len(lijst))
    return lijst.pop(_id)

def trek_kleur(lijst, slagkaarten):
    kleur = slagkaarten[0][0][0]
    for i, _kaart in enumerate(lijst):
        _kleur = _kaart[0]
        if _kleur is kleur:
            return lijst.pop(i)
    return trek_willekeurig(lijst)

#------- PRINT FUNCTIONS
def kaart_plat(kaart):
    return kaart[0]+str(kaart[1])

def kaartenprint(kaarten):
    _kaarten = [kaart_plat(kaart) for kaart in kaarten]
    print(" ".join(_kaarten))

def slagkaartenprint(slagkaarten):
    _kaarten = ""
    for slagkaart in slagkaarten:
        kaart, team = slagkaart
        _kaarten += team + kaart[0]+str(kaart[1]) + " "
    print(_kaarten)

def huidige_toestand(slagkaarten=None):
    print("------------------")
    print()
    print("Slag", sid, "in ronde", rid)
    print()
    print("Huidige score", (scoreA, scoreB))
    print()
    if sum([len(speler) for speler in spelers]) > 0:
        print("Speelkaarten, gesorteerd:")
        [kaartenprint(sorted(speler, key=lambda x: x[0])) for speler in spelers]
        print()
    print("Aantal kaarten nog te spelen:", list(map(len, spelers)))
    print()
    print("Slagkaarten:", "troef", troefkleur)
    slagkaartenprint(slagkaarten)
    print()

def korte_toestand(slagkaarten=None):
    print("------------------")
    print("Slag", sid, "in ronde", rid)
    print("Huidige score", (scoreA, scoreB))
    print("Slagkaarten:", "troef", troefkleur)
    slagkaartenprint(slagkaarten)
    print()


#------- SCORE FUNCTIONS
def scoor(game):
    _scoreA, _scoreB = 0, 0
    for slagkaart in game.slagkaarten:
        _id = game.kaarten.index(slagkaart[0][1])
        if slagkaart[1] == 'A':
            _scoreA += game.model[_id]
        else:
            _scoreB += game.model[_id]
    return _scoreA, _scoreB

def scoor_kaarten(game):
    aantal_troef = sum([slagkaart[0][0] is game.troefkleur 
        for slagkaart in game.slagkaarten])
    game.model = game.troefscores if aantal_troef > 0 else game.hoogstescores
    return scoor(game)


def speel_slag(game):
    game.slagkaarten = [None] * 4

    for i, team in zip(game.volgorde, game.teams):
        if game.slagkaarten == ([None] * 4):
            game.slagkaarten[i] = (trek_willekeurig(game.spelers[i]), team)
        else:
            game.slagkaarten[i] = (trek_kleur(
                    game.spelers[i], game.slagkaarten), team)

def speel_rondes(n):
    for i in range(n):
        for i in range(8):
            _scoreA, _scoreB = speel_slag()
            scoreA += _scoreA
            scoreB += _scoreB
            sid += 1

        print("Ronde-uitslag", (scoreA, scoreB))
        print("------------------")
        print("------------------")

        spelers, troefkleur = nieuwe_slag()

        rid += 1
    print("Einduitslag", (scoreA, scoreB))
    print("------------------")
    print("------------------")
    print("------------------")
    print("------------------")

def als_kleur(kleur):
    return colors.black if kleur in ["♠", "♣"] else colors.red
