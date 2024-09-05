# Selleks, et saada kasutajalt sisendit on pythonil sisseehitatud funktsionaalsus
# input()

# Trükime välja lause: "Mis on sinu nimi?" ning seejärel ootame kasutaja sisendit
input("Mis on sinu nimi?")
# Tulemusena küsitakse sisend, aga midagi erilist ei paista juhtuvat

# Selleks, et kasutaja sisendit saaks ka edaspidi kasutada defineerime muutuja "sisend"
sisend = input("Mis on sinu nimi?")
# Nüüd saame näiteks trükkida sisendi uuesti välja kasutades funktsiooni print()
print(sisend)
# Nüüd trükiti lisaks küsimusele välja ka sisendist saadud tekst

# Seejärel teksti saame saadud sisendit ka töödelda ja kokku liita
tere = "Tere, "
lause = tere + " " + sisend + "!"
print(lause)
# Tulemuseks saime lause (näiteks): Tere, Nipitiri!