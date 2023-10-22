from .baseUnit import BaseUnit

class coulomb(BaseUnit):
    
    base = "C"
    dimension = "charge"
    __name__ = "coulomb"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

charge_units = [coulomb]