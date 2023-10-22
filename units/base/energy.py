from .baseUnit import BaseUnit

class joule(BaseUnit):

    base = "J"
    dimension = "energy"
    __name__ = "joule"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class btu(BaseUnit):

    base = "BTU"
    dimension = "energy"
    __name__ = "btu"
    base_modifier = 0.000947817

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class calorie(BaseUnit):

    base = "cal"
    dimension = "energy"
    __name__ = "calorie"
    base_modifier = 1 / 4.184

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

energy_units = [joule, btu, calorie]