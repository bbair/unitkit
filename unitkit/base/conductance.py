from .baseUnit import BaseUnit, Dimension

class Conductance(Dimension):

    __name__ = "Conductance"

    def __init__(self):
        self.units = [siemens]
        self.base = siemens


class siemens(BaseUnit):

    base = "S"
    __name__ = "siemens"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Conductance())