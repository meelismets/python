# defineerime muutuja faili nimega, nõnda on seda hilejm mugavam muuta
konto_fail = "konto.txt"

def loe():
    fail = open(konto_fail, encoding="UTF-8")
    kontoseis = 0
    for rida in fail:
        kontoseis = int(rida)
    fail.close()
    return kontoseis

def salvesta(uus_kontoseis):
    fail = open(konto_fail, "w")
    kontoseis_kirjutamiseks = str(uus_kontoseis)
    fail.write(kontoseis_kirjutamiseks)
    fail.close()