from .baseUnit import BaseUnit, Dimension

class Current(Dimension):

    __name__ = "Current"

    def __init__(self):
        self.units = [ampere]
        self.base = ampere

class ampere(BaseUnit):
    
    base = "A"
    __name__ = "ampere"
    expanded = "C/s"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Current())