fail = open("kirjutatud.txt", encoding="UTF-8")
#loeme faili
loetud_fail = fail.read()

fail.close()
#tükeldame faili
tykeldatud_fail = loetud_fail.split("\n")

ridade_arv = len(tykeldatud_fail) - 1

for nr in range(0, ridade_arv, 3):
    print("Nimi: " + tykeldatud_fail[nr])
    print("Vanus: " + tykeldatud_fail[nr])

