from .baseUnit import BaseUnit, Dimension

class Pressure(Dimension):

    __name__ = "Pressure"

    def __init__(self):
        self.units = [pascal, atmosphere, mmHg, psi, bar]
        self.base = pascal

class pascal(BaseUnit):
    
    base = "Pa"
    __name__ = "pascal"
    expanded = "N/m2"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp,  dimension=Pressure())

class atmosphere(BaseUnit):

    base = "atm"
    __name__ = "atmosphere"
    base_modifier = 1 / 101325

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp,  dimension=Pressure())

class mmHg(BaseUnit):

    base = "mmHg"
    __name__ = "mmHg"
    base_modifier = atmosphere.base_modifier * 760

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp,  dimension=Pressure())

class torr(BaseUnit):

    base = "torr"
    __name__ = "torr"
    base_modifier = atmosphere.base_modifier * 760

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp,  dimension=Pressure())

class psi(BaseUnit):

    base = "psi"
    __name__ = "psi"
    base_modifier = atmosphere.base_modifier * 14.696

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp,  dimension=Pressure())

class bar(BaseUnit):

    base = "bar"
    __name__ = "bar"
    base_modifier = 1e-5

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp,  dimension=Pressure())