from .base import BaseUnit
from .parse import parse_units
from . import conversions, _utils

class Units:

    __name__ = "unit"

    def __init__(self, string: str = "", base_units: list[BaseUnit] = [], parse = True):
        self.string: str = string
        self.base_units: list[BaseUnit] = []

        if parse:
            self.string, self.base_units = parse_units(string)
        else:
            flattened = _flatten_unit_list(base_units)
            self.base_units = _combine_unit_list(flattened)

        # Take out any BaseUnits with an exponent of 0
        i = 0
        while i < len(self.base_units):
            if self.base_units[i].exp == 0:
                self.base_units.pop(i)
            else:
                i += 1

    def __str__(self):
        if self.is_unitless():
            return "(unitless)"
        
        string = []
        for u in sorted(self.base_units, reverse=True):
            string.append(str(u))
        
        return " ".join(string)
    
    def __mul__(self, other):
        new = Units()
        if isinstance(other, BaseUnit):
            for u in self.base_units:
                if u == other:
                    u = u * other
                if u:
                    new.base_units.append(u)
            if other not in self.base_units:
                new.base_units.append(other)      

        else:
            for u in self.base_units:
                if u in other.base_units:
                    same = [x for x in other.base_units if x == u][0]
                    u = u * same
                if u:
                    new.base_units.append(u)
            for u in other.base_units:
                if not u in self.base_units:
                    new.base_units.append(u)

        return new
    
    def __truediv__(self, other):
        temp = other.invert()
        return self * temp
    
    def is_unitless(self):
        return len(self.base_units) == 0

    def _flatten(self) -> list[BaseUnit]:
        flattened = _flatten_unit_list(self.base_units)
        return Units(base_units=flattened, parse=False)
    
    @property
    def dimension(self):
        dim_strs = []
        for u in self.base_units:
            if u.exp == 1:
                dim_strs.append(str(u.dimension))
            elif u.exp % 1 == 0:
                dim_strs.append(f"{u.dimension}^{int(u.exp)}")
            else:
                dim_strs.append(f"{u.dimension}^{u.exp}")
        return " ".join(dim_strs)
    
    def update_exp(self, exp):
        new = self.copy()
        for u in new.base_units:
            u.update_exp(exp)
        return new

    def invert(self):
        new = self.copy()
        for u in new.base_units:
            u.update_exp(-1)
        return new

    def copy(self):
        new = Units(string = self.string, parse=False)
        for u in self.base_units:
            new.base_units.append(u.copy())
        return new
    
    def simplify(self):
        remaining = self.base_units.copy()
        keep = []
        while len(remaining) > 0:
            canceled = False
            u = remaining.pop(0)

            i = 0
            while i < len(remaining):
                if conversions.can_convert(u * remaining[i]):
                    other = remaining.pop(i)
                    canceled = True
                    break
                elif conversions.can_convert(u / remaining[i]):
                    other = remaining.pop(i)
                    u.exp += other.exp
                else:
                    i += 1

            if not canceled:
                keep.append(u)
        return Units(base_units=keep, parse=False)
    
    def expand_all(self):
        new_base_units = []
        modifier = 1
        for u in self.base_units:

            u, to_dbase_modifier = u.to_dimension_base()
            modifier *= to_dbase_modifier

            if u.can_expand():
                expanded, expand_modifier = u.full_expand()
                modifier *= expand_modifier
                new_base_units.extend(expanded.base_units)
            else:
                new_base_units.append(u)

        return Units(base_units=new_base_units, parse=False), modifier
    
    def _combine(self):
        combined = _combine_unit_list(self.base_units)
        return Units(base_units=combined, parse=False)


class Value:

    __use_sigfigs__ = False

    def __init__(self, number, units = None, sigfigs = None):
        self.value = float(number) if number else number

        if not isinstance(units, Units):
            units = Units(units)
        self.units = units

        if sigfigs is None:
            sigfigs = _utils.count_sigfigs(number)
        self.sigfigs = sigfigs

    def __repr__(self):
        return f"Value({self.value}, '{self.units}')"
    
    def __str__(self):
        if self.__use_sigfigs__:
            return f"{self.roundsf().value} {self.units}"
        return f"{self.value} {self.units}"
    
    def __float__(self):
        return self.value

    def __int__(self):
        return int(self.value)
    
    def __eq__(self, other):
        return self.equals(other)
    
    def __neg__(self):
        return Value(-self.value, self.units.copy(), self.sigfigs)
    
    @_utils.ensure_value_input
    def __lt__(self, other):
        assert isinstance(other, Value)
        other = other.convert_units(self.units)
        return self.value < other.value
    
    @_utils.ensure_value_input
    def __gt__(self, other):
        assert isinstance(other, Value)
        other = other.convert_units(self.units)
        return self.value > other.value
    
    @_utils.ensure_value_input
    def __add__(self, other):
        assert isinstance(other, Value)
        other = other.convert_units(self.units)
        return Value(self.value + other.value, self.units, min([self.sigfigs, other.sigfigs]))
    
    @_utils.ensure_value_input
    def __radd__(self, other):
        return self.__add__(other)
    
    @_utils.ensure_value_input
    def __sub__(self, other):
        assert isinstance(other, Value)
        other = other.convert_units(self.units)
        return Value(self.value - other.value, self.units, min([self.sigfigs, other.sigfigs]))
    
    @_utils.ensure_value_input
    def __rsub__(self, other):
        assert isinstance(other, Value)
        return Value(other - self.value, self.units, self.sigfigs)
    
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Value(self.value * other, self.units, self.sigfigs)
        return Value(self.value * other.value, self.units * other.units, min([self.sigfigs, other.sigfigs]))
    
    def __rmul__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError()
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Value(self.value / other, self.units, self.sigfigs)
        return Value(self.value / other.value, self.units / other.units, min([self.sigfigs, other.sigfigs]))
    
    def __rtruediv__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError()
        return Value(other / self.value, self.units.invert(), self.sigfigs)
    
    def __pow__(self, exp):
        if isinstance(exp, Value):
            exp = exp.value
        return Value(self.value ** exp, self.units.update_exp(exp), self.sigfigs)
    
    def __round__(self, n = None):
        new = self.copy()
        new.value = round(new.value, n)
        return new
    
    def roundsf(self):
        if self.value:
            import sigfig
            return Value(sigfig.round(self.value, sigfigs = self.sigfigs), self.units, self.sigfigs)
        return self

    @_utils.force_unitless
    def log(self):
        import math
        return Value(math.log(self.value), None, self.sigfigs)
    
    @_utils.force_unitless
    def exp(self):
        import math
        return Value(math.exp(self.value), None, self.sigfigs)
    
    @_utils.ensure_value_input
    def equals(self, other, epsilon = 0.005):
        assert isinstance(other, Value)
        other = other.convert_units(self.units)
        return abs((self.value - other.value) / self.value) < epsilon
    
    def copy(self):
        new = Value(self.value, self.units.copy(), self.sigfigs)
        return new
    
    def convert_units(self, new_units, mw = None):
        return conversions.convert(self, new_units, mw)
    
    def to(self, new_units, mw = None):
        return self.convert_units(new_units, mw)
    
    def simplify_units(self):
        new_units = self.units.simplify()
        return self.to(new_units)
 
    
def use_sigfigs():
    try:
        import sigfig
        Value.__use_sigfigs__ = True
    except ModuleNotFoundError:
        print("The sigfig module was not found. Sigfig rounding will not be used.")


def _combine_unit_list(units: list[BaseUnit]):
    remaining = units.copy()
    combined = []

    while len(remaining) > 0:
        current = remaining.pop()
        i = 0

        while i < len(remaining):
            if current == remaining[i]:
                other = remaining.pop(i)
                current *= other

                if current is None:
                    break
            else:
                i += 1

        if current:
            combined.append(current)

    return combined


def _flatten_unit_list(units) -> list[BaseUnit]:
    return_lst: list[BaseUnit] = []
    for u in units:
        if isinstance(u, Units) and u.base_units:
            return_lst.extend(u.base_units)
        else:
            return_lst.append(u)
    return return_lst