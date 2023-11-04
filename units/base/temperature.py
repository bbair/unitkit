from .baseUnit import BaseUnit, Dimension

class Temperature(Dimension):

    __name__ = "Temperature"

    def __init__(self):
        self.units = [kelvin]
        self.base = kelvin

class kelvin(BaseUnit):

    base = "K"
    __name__ = "kelvin"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Temperature())