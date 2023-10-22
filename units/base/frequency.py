from .baseUnit import BaseUnit

class hertz(BaseUnit):
    
    base = "Hz"
    dimension = "frequency"
    __name__ = "hertz"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

frequency_units = [hertz]