from .baseUnit import BaseUnit

class kelvin(BaseUnit):

    base = "K"
    dimension = "temperature"
    __name__ = "kelvin"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

temperature_units = [kelvin]