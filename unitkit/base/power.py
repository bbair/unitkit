from .baseUnit import BaseUnit, Dimension

class Power(Dimension):

    __name__ = "Power"

    def __init__(self):
        self.units = [watt]
        self.base = watt

class watt(BaseUnit):
    
    base = "W"
    __name__ = "watt"
    expanded = "J/s"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Power())