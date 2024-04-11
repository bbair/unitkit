from .base import BaseUnit
from .parse import parse_units
from . import _sigfigs, conversions, _utils

class Units:
    """
    Represents a collection of base units and provides methods for manipulation and conversion.

    Parameters
    ----------
    string : str, optional
        A string representation of units (default is "").
    base_units : list[BaseUnit], optional
        A list of BaseUnit objects (default is []).
    parse : bool, optional
        Whether to parse the string representation of units (default is True).

    Attributes
    ----------
    string : str
        The string representation of units.
    base_units : list[BaseUnit]
        A list of BaseUnit objects representing the units.

    Methods
    -------
    is_unitless()
        Checks if the units are dimensionless.
    _flatten()
        Flattens nested units into a single list of base units.
    dimension()
        Calculates the dimension of the units.
    update_exp(exp)
        Updates the exponents of the base units.
    invert()
        Inverts the units.
    copy()
        Creates a copy of the Units object.
    simplify()
        Simplifies the units by combining similar units.
    expand_all()
        Expands all base units to their fundamental dimensions.
    _combine()
        Combines similar base units into a single unit.
    """

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
    """
    Represents a value with associated units and provides methods for arithmetic operations and unit conversions.

    Parameters
    ----------
    number : float
        The numerical value.
    units : Units, optional
        The associated units (default is None, i.e., unitless).
    sigfigs : int, optional
        The number of significant figures (default is None).

    Attributes
    ----------
    value : float
        The numerical value.
    units : Units
        The associated units.
    sigfigs : int
        The number of significant figures.

    Methods
    -------
    roundsf(n)
        Rounds the value to the specified number of significant figures.
    log()
        Computes the natural logarithm of the value.
    exp()
        Computes the exponential of the value.
    equals(other)
        Checks if the value is approximately equal to another value.
    copy()
        Creates a copy of the Value object.
    convert_units(new_units, mw)
        Converts the value to new units.
    to(new_units, mw)
        Converts the value to new units (alternative method).
    simplify_units()
        Simplifies the units associated with the value.
    """

    __use_sigfigs__ = False

    def __init__(self, number, units = None, sigfigs = None):
        """
        Initializes a Value object with a numerical value, associated units, and optional significant figures.
        
        Parameters
        ----------
        number : float
            The numerical value.
        units : str | Units, optional
            The associated units (default is None).
        sigfigs : int, optional
            The number of significant figures (default is None).
        """
        self.value = float(number) if number else number

        if not isinstance(units, Units):
            units = Units(units)
        self.units = units

        if sigfigs is None:
            sigfigs = _sigfigs.count(number)
        self.sigfigs = sigfigs

    def __repr__(self):
        return f"Value({self.value}, '{self.units}')"
    
    def __str__(self):
        if self.__use_sigfigs__:
            return f"{self.value:.{self.sigfigs - 1}e} {self.units}"
        return f"{self.value} {self.units}"
    
    def __format__(self, code: str):
        if code.endswith("f") or code.endswith("e"):
            return f"{self.value:{code}} {self.units}"
        raise Exception(f"Unsupported format code: '{code}'")
    
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
    
    def roundsf(self, n = None):
        """
        Rounds the value to the specified number of significant figures.

        Parameters
        ----------
        n : int, optional
            The number of significant figures to round to

        Returns
        -------
        Value
            The value rounded based on significant figures
        """
        if self.value:
            import sigfig
            if n is None:
                n = self.sigfigs
            return Value(sigfig.round(self.value, sigfigs=n), self.units, n)
        return self

    @_utils.force_unitless
    def log(self):
        """
        Computes the natural logarithm of the value.

        Returns
        -------
        Value
            The resulting value. This value will always be 
            unitless.
        """
        import math
        return Value(math.log(self.value), None, self.sigfigs)
    
    @_utils.force_unitless
    def exp(self):
        """
        Computes the exponential of the value.

        Returns
        -------
        Value
            The exponentiated value. This value will always be
            unitless.
        """
        import math
        return Value(math.exp(self.value), None, self.sigfigs)
    
    @_utils.ensure_value_input
    def equals(self, other, epsilon = 0.005):
        """
        Check if this value is equal to another (within the specified 
        relative tolerance).

        Returns
        -------
        bool
            True or False indicating if this value equals the other.
        """
        assert isinstance(other, Value)
        other = other.convert_units(self.units)
        return abs((self.value - other.value) / self.value) < epsilon
    
    def copy(self):
        """
        Create a deep copy of this value object.
        """
        new = Value(self.value, self.units.copy(), self.sigfigs)
        return new
    
    def convert_units(self, new_units, mw = None):
        """
        Convert the units of this value to new units.

        Parameters
        ----------
        new_units : str | Units
            The new units to convert to
        mw : Value, optional
            The molecular weight for conversions that require
            a molecular weight (e.g., converting from kg to mol)
        
        Returns
        -------
        Value
            A new value object with the original value converted 
            to the new units.
        """
        return conversions.convert(self, new_units, mw)
    
    def to(self, new_units, mw = None):
        """
        Convert the units of this value to new units.

        This method is simply another name for the `convert_units`
        method.

        Parameters
        ----------
        new_units : str | Units
            The new units to convert to
        mw : Value, optional
            The molecular weight for conversions that require
            a molecular weight (e.g., converting from kg to mol)
        
        Returns
        -------
        Value
            A new value object with the original value converted 
            to the new units.
        """
        return self.convert_units(new_units, mw)
    
    def simplify_units(self):
        """
        Simplify the units by combining specific units with the
        same dimensions.

        THIS METHOD IS UNTESTED.

        Returns
        -------
        Value
            A new value with simplified units.
        """
        new_units = self.units.simplify()
        return self.to(new_units)
 
    
def use_sigfigs():
    """
    Enables the usage of significant figures rounding in Value objects.
    """
    try:
        import sigfig
        Value.__use_sigfigs__ = True
    except ModuleNotFoundError:
        print("The sigfig module was not found. Sigfig rounding will not be used.")


def _combine_unit_list(units: list[BaseUnit]):
    """
    Combines similar BaseUnit objects in a list.

    Parameters
    ----------
    units : list[BaseUnit]
        A list of BaseUnit objects.

    Returns
    -------
    list[BaseUnit]
        A list of combined BaseUnit objects.
    """
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
    """
    Flattens nested units into a single list of BaseUnit objects.

    Parameters
    ----------
    units : object
        The input units, which could be nested.

    Returns
    -------
    list[BaseUnit]
        A flattened list of BaseUnit objects.
    """
    return_lst: list[BaseUnit] = []
    for u in units:
        if isinstance(u, Units) and u.base_units:
            return_lst.extend(u.base_units)
        else:
            return_lst.append(u)
    return return_lst