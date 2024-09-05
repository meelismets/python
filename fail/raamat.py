from urllib.request import urlopen

failVeebis = urlopen("https://kool.metz.ee/todejaoigus.txt")
baidid = failVeebis.read()
tekst = baidid.decode()  # baitidest saab sõne
ridadeKaupa = tekst.splitlines()  # sõne jaotatakse reavahetuse kohtadelt

loendur_tode = 0


for rida in ridadeKaupa:
    if rida != "":
        sonad = rida.split()  # rea sõnad järjendisse
        for sona in sonad:
            print(sona)