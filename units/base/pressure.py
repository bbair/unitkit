from .baseUnit import BaseUnit

class pascal(BaseUnit):
    
    base = "Pa"
    dimension = "pressure"
    __name__ = "pascal"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class atmosphere(BaseUnit):

    base = "atm"
    dimension = "pressure"
    __name__ = "atmosphere"
    base_modifier = 1 / 101325

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class mmHg(BaseUnit):

    base = "mmHg"
    dimension = "pressure"
    __name__ = "mmHg"
    base_modifier = atmosphere.base_modifier * 760

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class torr(BaseUnit):

    base = "torr"
    dimension = "pressure"
    __name__ = "torr"
    base_modifier = atmosphere.base_modifier * 760

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class psi(BaseUnit):

    base = "psi"
    dimension = "pressure"
    __name__ = "psi"
    base_modifier = atmosphere.base_modifier * 14.696

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class bar(BaseUnit):

    base = "bar"
    dimension = "pressure"
    __name__ = "bar"
    base_modifier = 1e-5

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

pressure_units = [pascal, atmosphere, mmHg, psi, bar]