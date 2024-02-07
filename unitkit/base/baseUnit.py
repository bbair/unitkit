class BaseUnit:

    prefixes = ["n", "u", "m", "c", "d", "k", "M", ""]
    prefix_modifiers = [1e9, 1e6, 1e3, 1e2, 1e1, 1e-3, 1e-6, 1]
    base = ""
    base_modifier = 1
    shift_modifier = 0
    expanded = ""

    def __init__(self, prefix = "", exp = 1.0, dimension = None):
        self.prefix = prefix
        self.exp = exp
        self.dimension = dimension
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
    
    def __bool__(self):
        return True
    

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
        copy.expanded = self.expanded
        return copy

    def invert(self):
        new = self.copy()
        new.update_exp(-1)
        return new

    def _mod(self):
        return self._pre_mod() * self._base_mod()
    
    def _pre_mod(self):
        return self.prefix_modifier ** self.exp
    
    def _base_mod(self):
        return self.base_modifier ** self.exp
    
    def can_expand(self):
        return self.expanded != ""
    
    def expand(self):
        from ..main import Units
        if self.can_expand():
            expanded = Units(self.expanded).update_exp(self.exp)
            return expanded
        return Units(self.prefix + self.base)
    
    def full_expand(self):
        if self.can_expand():
            expanded, modifier = self.expand().expand_all()
            return expanded, modifier
        return self, 1
    
    def to_dimension_base(self):
        dbase_unit = self.dimension.base(prefix="", exp=self.exp)
        modifier = self._mod()
        return dbase_unit, modifier


class Custom(BaseUnit):

    def __init__(self, base, dimension, name, base_modifier = 1, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)
        self.base = base

        if isinstance(dimension, Dimension):
            self.dimension = dimension
        else:
            self.dimension = _get_dimension(dimension)

        self.__name__ = name
        self.base_modifier = base_modifier

    def __call__(self, prefix = "", exp = 1):
        return Custom(self.base, self.dimension, self.__name__, self.base_modifier, prefix, exp)
    

class Dimension:

    base: BaseUnit
    __name__ = ""

    def __init__(self):
        self.units = []

    def __str__(self):
        return self.__name__
    
    def __eq__(self, other):
        return self.__name__ == other.__name__
    
    def __hash__(self):
        return hash(self.__name__)
    

def _get_dimension(name: str) -> Dimension:
    from . import all_dimensions

    for dim in all_dimensions:
        if dim.__name__.lower() == name.lower():
            return dim()
    
    print(f"Dimension '{name}' not found among available dimensions.")
    return None