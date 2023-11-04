from .baseUnit import BaseUnit, Dimension

class Frequency(Dimension):

    __name__ = "Frequency"

    def __init__(self):
        self.units = [hertz]
        self.base = hertz

class hertz(BaseUnit):
    
    base = "Hz"
    __name__ = "hertz"
    expanded = "s^-1"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Frequency())