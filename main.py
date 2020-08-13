import random


# TODO: GROOT pygame en weergave

# ---------------INDEX
# -- 1 RESET
# -- 2 CARD/DEAL
# -- 3 PRINT
# -- 4 SCORE
# -- 5 PLAY
# ---------------END


# Zodat deze ook globaal toegankelijk zijn
kleuren = ["♠", "♥", "♦", "♣"]
aantallen = ["A", 10, "K", "Q", "J", 9, 8, 7]

# -----------------------
# ---- 1. RESET FUNCTIONS
# -----------------------
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

# Nog wat meer globale variabelen
spelers, troefkleur = nieuwe_slag()
rid = 0 # ronde id
sid = 0 # slag id

scoreA = 0
scoreB = 0

# TODO: Waar was dit voor? Kan het weg?
gewonnenA = []
gewonnenB = []

teams    = ["A", "B", "A", "B"]
volgorde = [0, 1, 2, 3]

# ---------------------------
# ---- 2. CARD/DEAL FUNCTIONS
# ---------------------------
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

# -----------------------
# ---- 3. PRINT FUNCTIONS
# -----------------------u
def kaartenprint(kaarten):
    _kaarten = [kaart[0]+str(kaart[1]) for kaart in kaarten]
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

# -----------------------
# ---- 4. SCORE FUNCTIONS
# -----------------------
kaarten =  [7, 8, 9, 10, 'J', 'Q', 'K', 'A']
troefscores = [0, 0, 14, 10, 11, 20, 4, 3]
hoogstescores = [0, 0, 0, 10, 2, 3, 4, 11]

def scoor(slagkaarten, model):
    _scoreA, _scoreB = 0, 0
    for slagkaart in slagkaarten:
        _id = kaarten.index(slagkaart[0][1])
        if slagkaart[1] == 'A':
            _scoreA += model[_id]
        else:
            _scoreB += model[_id]
    return _scoreA, _scoreB

def scoor_kaarten(slagkaarten):
    aantal_troef = sum([slagkaart[0][0] is troefkleur for slagkaart in slagkaarten])
    model = troefscores if aantal_troef > 0 else hoogstescores
    return scoor(slagkaarten, model)

# ----------------------
# ---- 5. PLAY FUNCTIONS
# ----------------------
def speel_slag():
    slagkaarten = [None] * 4

    for i, team in zip(volgorde, teams):
        if slagkaarten == ([None] * 4):
            slagkaarten[i] = (trek_willekeurig(spelers[i]), team)
        else:
            slagkaarten[i] = (trek_kleur(spelers[i], slagkaarten), team)

    # huidige_toestand(slagkaarten)
    korte_toestand(slagkaarten)

    slagscoreA, slagscoreB = scoor_kaarten(slagkaarten)
    return slagscoreA, slagscoreB

for i in range(3):
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
