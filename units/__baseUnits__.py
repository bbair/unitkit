class BaseUnit:

    prefixes = ["n", "u", "m", "c", "d", "k", "M", ""]
    prefix_modifiers = [1e9, 1e6, 1e3, 1e2, 1e1, 1e-3, 1e-6, 1]
    base = ""
    dimension = ""
    base_modifier = 1

    def __init__(self, prefix = "", exp = 1.0):
        self.prefix = prefix
        self.exp = exp
        self.prefix_modifier = self.prefix_modifiers[self.prefixes.index(prefix)]

    def __str__(self):
        return f"{self.prefix}{self.base}^{self.exp}" if self.exp != 1 else f"{self.prefix}{self.base}"
    
    def __repr__(self):
        string = f"{self.__name__}("
        kwargs = []
        if self.prefix != "":
            kwargs.append(f"prefix = '{self.prefix}'")
        if self.exp != 1.0:
            kwargs.append(f"exp = {self.exp}")
        string += ", ".join(kwargs)
        string += ")"
        return string
    
    def __eq__(self, other):
        return self.prefix == other.prefix and self.base == other.base
    
    def __mul__(self, other):
        from .main import Units
        if isinstance(other, Units):
            return other * self
        
        if self == other:
            new = self.copy()
            new.exp += other.exp
            if new.exp == 0:
                return None
            else:
                return new
            
        return Units(base_units=[self, other], parse=False)
    
    def __truediv__(self, other):
        temp = other.invert()
        return self * temp

    def try_match(unit_type, token: str):
        if not unit_type.base in token:
            return False
        token = token.replace(unit_type.base, "", 1)

        prefix = ""
        for p in BaseUnit.prefixes:
            if p in token:
                token = token.replace(p, "", 1)
                prefix = p
                break
        
        if token == "":
            return unit_type(prefix = prefix)
        
        if not (token.isdigit() or token.isdecimal()):
            return False
        exp = float(token)

        return unit_type(prefix = prefix, exp = exp)
    
    def update_exp(self, exp):
        self.exp *= exp

    def copy(self):
        return eval(self.__repr__())

    def invert(self):
        new = self.copy()
        new.update_exp(-1)
        return new

    def mod(self):
        return (self.base_modifier * self.prefix_modifier) ** self.exp



class meter(BaseUnit):

    base = "m"
    dimension = "length"
    __name__ = "meter"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

        
class kelvin(BaseUnit):

    base = "K"
    dimension = "temperature"
    __name__ = "kelvin"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)


class joule(BaseUnit):

    base = "J"
    dimension = "energy"
    __name__ = "joule"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)


class pascal(BaseUnit):
    
    base = "Pa"
    dimension = "pressure"
    __name__ = "pascal"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)


class gram(BaseUnit):
    
    base = "g"
    dimension = "mass"
    __name__ = "gram"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)


class mol(BaseUnit):
    
    base = "mol"
    dimension = "amount"
    __name__ = "mol"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)


class gramMol(BaseUnit):
    
    base = "gmol"
    dimension = "amount"
    __name__ = "gmol"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)


class newton(BaseUnit):
    
    base = "N"
    dimension = "force"
    __name__ = "newton"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)


class second(BaseUnit):
    
    base = "s"
    dimension = "time"
    __name__ = "second"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)


class watt(BaseUnit):
    
    base = "W"
    dimension = "power"
    __name__ = "watt"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)


class coulomb(BaseUnit):
    
    base = "C"
    dimension = "charge"
    __name__ = "coulomb"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)


class hertz(BaseUnit):
    
    base = "Hz"
    dimension = "frequency"
    __name__ = "hertz"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)


class custom(BaseUnit):

    def __init__(self, base, dimension, name, base_modifier = 1, prefix = "", exp = 1):
        self.base = base
        self.dimension = dimension
        self.__name__ = name
        self.base_modifier = base_modifier
        super().__init__(prefix = prefix, exp = exp)

    def __call__(self, prefix = "", exp = 1):
        return custom(self.base, self.dimension, self.__name__, self.base_modifier, prefix, exp)


all_base_units = [meter, kelvin, joule, pascal, gram, mol, gramMol, newton, second, watt, coulomb, hertz]