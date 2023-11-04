from .baseUnit import BaseUnit, Dimension

class Energy(Dimension):

    __name__ = "Energy"

    def __init__(self):
        self.units = [joule, btu, calorie]
        self.base = joule

class joule(BaseUnit):

    base = "J"
    __name__ = "joule"
    expanded = "N*m"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Energy())

class btu(BaseUnit):

    base = "BTU"
    
    __name__ = "btu"
    base_modifier = 0.000947817

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Energy())

class calorie(BaseUnit):

    base = "cal"
    __name__ = "calorie"
    base_modifier = 1 / 4.184

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Energy())