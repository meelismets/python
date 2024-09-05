# impordime funktsioonid mis asuvad teistes failides
# näiteks failsit tervitus.py impordime funktsiooni tervitus
from tervitus import tervita
from autoriseerimine import kontrolli_pini
from valikud import tee_valik

# defineerime vajalikud muutujad
# näiteks muutuja, mis hoiab pangaautomaadi töös.
# nimetame selle automaatT88tab ning väärtustame tema väärtusega True ehk tõene.
automaatT88tab = True


# käivitame funktsiooni tervita, et kuvada kasutajale informatsiooni
tervita()


# defineerime funktsiooni pangaautomaadi mootoriks, nimetame ta näiteks start
def start():
    # teeme while tsükli, mis töötab senikaua, kui soovime pangaatomaati töös hoida
    while automaatT88tab:
        # kontrollime kas kasutaja on panka sisse loginud ja õige pini sisestanud
        # selleks kasutame teses failis defineeritud funktsioon kontrolli pini
        pin_6ige = kontrolli_pini()
        #kontrollime kas pin oli ikka õige
        if not pin_6ige:
            # Kui me ei saanud kasutajalt õiget pini, teavitame kasutajat programmis sulgemisest
            print("Sa ei teadnud õiget PIN koodi. Programm sulgub. Head aega!")
            # siis paneme programmi kinni
            exit()
        # Kui pin oli õige, siis programm läheb edasi ja pakub valikuid
        tee_valik()

# käivitame pangaautomaadi mootori
start()

