from .baseUnit import BaseUnit

class watt(BaseUnit):
    
    base = "W"
    dimension = "power"
    __name__ = "watt"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

power_units = [watt]