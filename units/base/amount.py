from .baseUnit import BaseUnit

class mol(BaseUnit):
    
    base = "mol"
    dimension = "amount"
    __name__ = "mol"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class gramMol(BaseUnit):
    
    base = "gmol"
    dimension = "amount"
    __name__ = "gmol"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

amount_units = [mol, gramMol]