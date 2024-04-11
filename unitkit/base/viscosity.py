from .baseUnit import BaseUnit, Dimension

class Viscosity(Dimension):

    __name__ = "Viscosity"

    def __init__(self):
        self.units = [poise]
        self.base = poise

class poise(BaseUnit):
    
    base = "P"
    __name__ = "poise"
    expanded = "dPa*s"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Viscosity())