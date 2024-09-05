# defineerime pini, mis on automaadi arvates õige, see mille kasutaja peaks sisestama
ootatud_pin = "1234"

# defineerime funktsiooni kysi_pini
def kysi_pini():
    # defineerime muutuja sisestatud_pin ja tagastame selle funktsiooni input kasutamisel saadud kasutaja sisendi
    return input("Palun sisesta pin kood:")

# defineerime funktsiooni v6rdle_pine
# sisendiks kasutame kahte muutujat: sisestatud_pin ja ootatud_pin
# neid saame funktsiooni sees kasutada ning ühtlasi funktsiooni välja kutsudes kaasa anda
def v6rdle_pine(sisestatud_pin, ootatud_pin):
    if (sisestatud_pin == ootatud_pin):
        print("Pin õige!")
        return True
    else:
        print("Vale pin!")
        return False

# defineerime funktsiooni kontrolli_pini
def kontrolli_pini():
    # kontrolli teostame mitte rohkem kui lubatud arv kordi
    # defineerime muutuja ja väärtustame mitu korda võiks lubada
    kordi_alles = 3
    # käivitame tsükli
    while kordi_alles > 0:
        # küsime kasutajalt pini, selleks käivitame meetodi, väärtustame sellega muutja sisestatud_pin
        sisestatud_pin = kysi_pini()
        # nüüd kontrollime kas pin on ikka sama kutsudes välja funktsiooni v6rdle_pine
        # saadud vastuse väärtustame muutujale pin_6ige
        pin_6ige = v6rdle_pine(sisestatud_pin, ootatud_pin)
        # nüüd kontollime kas pin oli juhtumisi vale, siis võiks lubada veel proovida näteks 3 korda
        if pin_6ige:
            # Kui pin õige siis tagastame tõese väärtuse
            return True
        else:
            # kui pin oli vale, siis vähendame loendurit
            kordi_alles = kordi_alles - 1
            # Trükime välja ka kasutajale teavituse
            # Pane tähele, t kordi_alles on arvuline väärtus, kasutame funktsiooni str(), et muuta arv tekstiks
            print("Saad veel proovida " + str(kordi_alles) + " korda!")
    # Kõige lõpus tagastame väära tulemuse, kuna oleme jõudnud funktsiooni lõppu saamata kasutajalt õiget pin koodi
    return False


