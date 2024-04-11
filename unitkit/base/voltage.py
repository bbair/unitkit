from .baseUnit import BaseUnit, Dimension

class Voltage(Dimension):

    __name__ = "Voltage"

    def __init__(self):
        self.units = [volt]
        self.base = volt

class volt(BaseUnit):
    
    base = "V"
    __name__ = "volt"
    expanded = "J/C"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Voltage())