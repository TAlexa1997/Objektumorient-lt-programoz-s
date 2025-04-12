from abc import ABC

class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: float):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
