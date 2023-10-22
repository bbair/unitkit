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
        exp = int(self.exp) if int(self.exp) == self.exp else self.exp
        return f"{self.prefix}{self.base}^{exp}" if self.exp != 1 else f"{self.prefix}{self.base}"
    
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
    

    # Comparison functions for sorting a list of BaseUnits
    # ----------------------------------------------------
    def __lt__(self, other):
        return self.exp < other.exp
    
    def __le__(self, other):
        return self.exp <= other.exp
    
    def __gt__(self, other):
        return self.exp > other.exp
    
    def __ge__(self, other):
        return self.exp >= other.exp
    # ----------------------------------------------------
    

    def __mul__(self, other):
        from ..main import Units
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
        copy = BaseUnit(self.prefix, self.exp)
        copy.base_modifier = self.base_modifier
        copy.base = self.base
        copy.dimension = self.dimension
        copy.__name__ = self.__name__
        return copy

    def invert(self):
        new = self.copy()
        new.update_exp(-1)
        return new

    def mod(self):
        return (self.base_modifier * self.prefix_modifier) ** self.exp
    

class custom(BaseUnit):

    def __init__(self, base, dimension, name, base_modifier = 1, prefix = "", exp = 1):
        self.base = base
        self.dimension = dimension
        self.__name__ = name
        self.base_modifier = base_modifier
        super().__init__(prefix = prefix, exp = exp)

    def __call__(self, prefix = "", exp = 1):
        return custom(self.base, self.dimension, self.__name__, self.base_modifier, prefix, exp)