from urllib.request import urlopen

failVeebis = urlopen("https://kool.metz.ee/todejaoigus.txt")
baidid = failVeebis.read()
tekst = baidid.decode()  # baitidest saab sõne
ridadeKaupa = tekst.splitlines()  # sõne jaotatakse reavahetuse kohtadelt
t2isread = 0
tyhiread = 0
kokkuread = 0
kokku = 0
tode = 0
oigus = 0
oigus1 = 0
oigus2 = 0
pearu = 0
pearu1 = 0

for rida in ridadeKaupa:  # ridade kaupa
    sonad = rida.split()  # rea sõnad järjendisse
    if rida != "":
        t2isread += 1
    else:
        tyhiread += 1
    for s in sonad:  # sõnade kaupa
        kokku += 1
        if s == "tõde" or s == "Tõde":
            tode += 1
        if s == "õigus" or s == "Õigus":
            oigus += 1
        # sõna algab õigus
        if s.lower().startswith("õigus"):
            oigus1 += 1
        # sõna sisaldab õigus
        if "õigus" in s.lower():
            oigus2 += 1
        if s == "Pearu":
            pearu1 += 1
        if "Pearu" in s:
            pearu += 1
print("Ridu kokku", len(ridadeKaupa))
print("Tyhjad read", tyhiread)
print("Täis read", t2isread)
print("Täis tyhi read kokku", t2isread + tyhiread)
print("Failis sõnu kokku on", kokku)
print("Failis sõna 'tõde' on", tode, "korda.")
print("Failis sõna 'õigus' on", oigus, "korda.")
print("Failis sõna 'õigus' on", oigus1, "korda.")
print("Failis sõna 'õigus' on", oigus2, "korda.")
print("Failis sõna 'Pearu' on", pearu, "korda.")
print("Failis sõna 'Pearu' on", pearu1, "korda.")

failVeebis.close()