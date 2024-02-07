from .baseUnit import BaseUnit, Dimension

class Volume(Dimension):

    __name__ = "Volume"

    def __init__(self):
        self.units = [liter, gallon]
        self.base = liter

class liter(BaseUnit):
    
    base = "L"
    __name__ = "liter"
    expanded = "dm^3"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Volume())

class gallon(BaseUnit):
    
    base = "gal"
    __name__ = "gallon"
    base_modifier = 1 / 3.785

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Volume())