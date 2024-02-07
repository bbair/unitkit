from .baseUnit import BaseUnit, Dimension

class Mass(Dimension):

    __name__ = "Mass"

    def __init__(self):
        self.units = [gram, poundMass]
        self.base = gram

class gram(BaseUnit):
    
    base = "g"
    __name__ = "gram"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Mass())

class poundMass(BaseUnit):

    base = "lbm"
    __name__ = "poundMass"
    base_modifier = 0.00220462

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Mass())