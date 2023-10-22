from .baseUnit import BaseUnit

class liter(BaseUnit):
    
    base = "L"
    dimension = "volume"
    __name__ = "liter"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class gallon(BaseUnit):
    
    base = "gal"
    dimension = "volume"
    __name__ = "gallon"
    base_modifier = 1 / 3.785

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

volume_units = [liter, gallon]