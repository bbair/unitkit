from .baseUnit import BaseUnit

class gram(BaseUnit):
    
    base = "g"
    dimension = "mass"
    __name__ = "gram"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class poundMass(BaseUnit):

    base = "lbm"
    dimension = "mass"
    __name__ = "poundMass"
    base_modifier = 0.00220462

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

mass_units = [gram, poundMass]