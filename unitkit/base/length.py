from .baseUnit import BaseUnit, Dimension

class Length(Dimension):

    __name__ = "Length"

    def __init__(self):
        self.units = [meter, feet, inch, yard]
        self.base = meter

class meter(BaseUnit):

    base = "m"
    __name__ = "meter"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Length())

class feet(BaseUnit):

    base = "ft"
    __name__ = "feet"
    base_modifier = 3.28084

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Length())

class inch(BaseUnit):

    base = "in"
    __name__ = "inch"
    base_modifier = feet.base_modifier * 12

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Length())

class yard(BaseUnit):

    base = "yrd"
    __name__ = "yard"
    base_modifier = feet.base_modifier / 3

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Length())