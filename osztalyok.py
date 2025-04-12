from abc import ABC

class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float):
        super().__init__(jaratszam, celallomas, jegyar)

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float):
        super().__init__(jaratszam, celallomas, jegyar)

class LegiTarsasag:
    def __init__(self, nev: str):
        self.nev = nev
        self.jaratok = []

class JegyFoglalas:
    def __init__(self, utas_nev: str, jarat: Jarat, datum: str):
        self.utas_nev = utas_nev
        self.jarat = jarat
        self.datum = datum
