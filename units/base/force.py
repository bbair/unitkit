from .baseUnit import BaseUnit

class newton(BaseUnit):
    
    base = "N"
    dimension = "force"
    __name__ = "newton"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

force_units = [newton]