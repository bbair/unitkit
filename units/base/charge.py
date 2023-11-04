from .baseUnit import BaseUnit, Dimension

class Charge(Dimension):

    __name__ = "Charge"

    def __init__(self):
        self.units = [coulomb]
        self.base = coulomb

class coulomb(BaseUnit):
    
    base = "C"
    __name__ = "coulomb"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Charge())