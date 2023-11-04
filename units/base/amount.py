from .baseUnit import BaseUnit, Dimension

class Amount(Dimension):

    __name__ = "Amount"

    def __init__(self):
        self.units = [mol, gramMol]
        self.base = mol

class mol(BaseUnit):
    
    base = "mol"
    __name__ = "mol"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Amount())

class gramMol(BaseUnit):
    
    base = "gmol"
    __name__ = "gmol"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Amount())

amount_units = [mol, gramMol]