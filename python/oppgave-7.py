# Før

# avstand_kilometer = input("Skriv inn avstand i kilometer: ")
# tid_minutter = input("Skriv inn tid i minutter: ")
# tempo = tid_minutter/avstand_kilometer
# print(f"Tempoet ditt var {tempo} minutter pr. kilometer")

# Etter

avstand_kilometer = float(input("Skriv inn avstand i kilometer: "))
tid_minutter = float(input("Skriv inn tid i minutter: "))
tempo = tid_minutter/avstand_kilometer
kmh = (avstand_kilometer/tid_minutter)*60
print(f"Tempoet ditt var {tempo} minutt(er) pr. kilometer")
print(f"Du gikk med en hastighet på {kmh} km/h")