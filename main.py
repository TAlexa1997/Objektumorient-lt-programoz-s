from osztalyok import BelfoldiJarat, NemzetkoziJarat, LegiTarsasag, JegyFoglalas

lt = LegiTarsasag("SkyFly Airlines")

jarat1 = BelfoldiJarat("BF123", "Budapest", 15000)
jarat2 = BelfoldiJarat("BF456", "Debrecen", 12000)
jarat3 = NemzetkoziJarat("INT789", "London", 55000)

lt.jaratok.append(jarat1)
lt.jaratok.append(jarat2)
lt.jaratok.append(jarat3)

foglalasok = [
    JegyFoglalas("Kiss Anna", jarat1, "2025-05-01"),
    JegyFoglalas("Nagy Béla", jarat1, "2025-05-01"),
    JegyFoglalas("Tóth László", jarat2, "2025-05-02"),
    JegyFoglalas("Kovács Júlia", jarat2, "2025-05-02"),
    JegyFoglalas("Szabó Péter", jarat3, "2025-05-03"),
    JegyFoglalas("Farkas Gábor", jarat3, "2025-05-03")
]

def menu():
    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Válassz egy lehetőséget (1-4): ")

        if valasztas == "1":
            jegy_foglalasa()
        elif valasztas == "2":
            foglalas_lemondasa()
        elif valasztas == "3":
            listaz_foglalasokat()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás, próbáld újra!")
            
            

