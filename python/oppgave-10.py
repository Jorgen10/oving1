def tallverdi():
    try:
        tegn = input("Skriv inn en bokstav: ")
        if len(tegn) < 1:
            print("Du må skrive inn en bokstav!")
            return tallverdi()
        if len(tegn) > 1:
            print("Du har for mange bokstaver!")
            return tallverdi()
        return ord(tegn)
    except:
        return tallverdi()

print(tallverdi())