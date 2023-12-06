from .baseUnit import BaseUnit, Dimension

class Amount(Dimension):

    __name__ = "Amount"

    def __init__(self):
        self.units = [mol, gramMol, poundMol]
        self.base = mol

class mol(BaseUnit):
    
    base = "mol"
    __name__ = "mol"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Amount())

class gramMol(BaseUnit):
    
    base = "gmol"
    __name__ = "gramMol"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Amount())

class poundMol(BaseUnit):

    base = "lbmol"
    __name__ = "poundMol"
    base_modifier = 0.00220462

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Amount())   