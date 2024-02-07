from .baseUnit import BaseUnit, Dimension

class Force(Dimension):

    __name__ = "Force"

    def __init__(self):
        self.units = [newton]
        self.base = newton

class newton(BaseUnit):
    
    base = "N"
    __name__ = "newton"
    expanded = "kg*m/s2"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Force())