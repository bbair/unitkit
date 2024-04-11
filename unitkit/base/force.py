from .baseUnit import BaseUnit, Dimension

class Force(Dimension):

    __name__ = "Force"

    def __init__(self):
        self.units = [newton, dyne, poundForce]
        self.base = newton

class newton(BaseUnit):
    
    base = "N"
    __name__ = "newton"
    expanded = "kg*m/s2"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Force())

class dyne(BaseUnit):

    base = "dyn"
    __name__ = "dyne"
    base_modifier = 1e5

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Force())

class poundForce(BaseUnit):

    base = "lbf"
    __name__ = "poundForce"
    base_modifier = 0.224809

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Force())