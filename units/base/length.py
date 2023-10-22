from .baseUnit import BaseUnit

class meter(BaseUnit):

    base = "m"
    dimension = "length"
    __name__ = "meter"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class feet(BaseUnit):

    base = "ft"
    dimension = "length"
    __name__ = "feet"
    base_modifier = 3.28084

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class inch(BaseUnit):

    base = "in"
    dimension = "length"
    __name__ = "inch"
    base_modifier = feet.base_modifier * 12

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class yard(BaseUnit):

    base = "yrd"
    dimension = "length"
    __name__ = "yard"
    base_modifier = feet.base_modifier / 3

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)    

length_units = [meter, feet, inch, yard]