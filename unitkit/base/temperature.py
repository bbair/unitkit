from .baseUnit import BaseUnit, Dimension

class Temperature(Dimension):

    __name__ = "Temperature"

    def __init__(self):
        self.units = [kelvin, celsius, celsius2, fahrenheit, fahrenheit2, rankine, rankine2]
        self.base = kelvin


class kelvin(BaseUnit):

    base = "K"
    __name__ = "kelvin"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Temperature())


class celsius(BaseUnit):

    base = "°C"
    __name__ = "celsius"
    shift_modifier = 273.15

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Temperature())


class celsius2(BaseUnit):

    base = "degC"
    __name__ = "celsius"
    shift_modifier = celsius.shift_modifier

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Temperature())


class fahrenheit(BaseUnit):

    base = "°F"
    __name__ = "fahrenheit"
    base_modifier = 9 / 5
    shift_modifier = celsius.shift_modifier * base_modifier - 32

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Temperature())


class fahrenheit2(BaseUnit):

    base = "degF"
    __name__ = "fahrenheit"
    base_modifier = fahrenheit.base_modifier
    shift_modifier = fahrenheit.shift_modifier

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Temperature())


class rankine(BaseUnit):

    base = "°R"
    __name__ = "rankine"
    base_modifier = fahrenheit.base_modifier
    shift_modifier = fahrenheit.shift_modifier - 459.67

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Temperature())


class rankine2(BaseUnit):

    base = "degR"
    __name__ = "rankine"
    base_modifier = rankine.base_modifier
    shift_modifier = rankine.shift_modifier

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Temperature())