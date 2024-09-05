# Defineerime funktsiooni, mis kuvab kasutajale valikud
def n2ita_valikuid():
    print("Vali üks valikutest sisestades numbri 1-3:")
    print("1 - näita konto seisu")
    print("2 - võta raha välja")
    print("3 - välju programmist")

# Defineerime funktsiooni, kuidas käituda kui valiti 1
def valik_1():
    print("Valisid 1 - näita konto seisu")

# Defineerime funktsiooni, kuidas käituda kui valiti 2
def valik_2():
    print("Valisid 2 - võta raha välja")

# Defineerime funktsiooni, kuidas käituda kui valiti 3
def valik_3():
    print("Valisid 3 - välju programmist")
    print("Head aega!")
    # kasutame programmist väljumiseks funktsiooni exit()
    exit()

# Defineerime funktsiooni, kuidas käituda kui valik oli vale või olematu
def valik_vale():
    print("Sellist valikut ei pakutud sulle ju!")

# Defineerime funktsiooni mis küsib kasutajalt valiku ja otsustab, mida vastusega teha
def tee_valik():
    n2ita_valikuid()
    # küsime kasutajalt valikut, seekord loeme valiku sisse arvulisel kujul kasutame funktsiooni int()
    kasutaja_valik = int(input("Sisesta valik: "))
    if kasutaja_valik == 1:
        valik_1()
    elif kasutaja_valik == 2:
        valik_2()
    elif kasutaja_valik == 3:
        valik_3()
    else:
        valik_vale()

    # Kui valik tehtud, võime pakkuda kasutajale uuesti valikut, jah, funktsioon saab ise ennast samuti käivitada
    # Sellist funktsiooni käivitamist kutsutakse rekursiivseks käivituseks
    tee_valik()
