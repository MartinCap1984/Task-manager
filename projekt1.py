ukoly = []

def hlavni_menu():
    while True:
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        volba = input("Zadejte volbu: ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ")
        popis = input("Popis úkolu: ")
        if nazev and popis:
            ukoly.append({"nazev": nazev, "popis": popis})
            print("Úkol byl přidán.")
            break
        else:
            print("Prázdný vstup, zkuste to znovu.")

def zobrazit_ukoly():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        for i, ukol in enumerate(ukoly, start=1):
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
    print("")

def odstranit_ukol():
    zobrazit_ukoly()
    if not ukoly:
        return
    while True:
        try:
            cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= cislo <= len(ukoly):
                del ukoly[cislo - 1]
                print("Úkol byl odstraněn.")
                break
            else:
                print("Neplatné číslo úkolu, zkuste to znovu.")
        except ValueError:
            print("Neplatný vstup, zadejte číslo úkolu.")

if __name__ == "__main__":
    hlavni_menu()
