import warnings

from . import conversions

def ensure_value_input(f):
    """A decorator to make sure inputs to comparison
    functions in the Value class are a Value object.
    """
    def wrapper(val, input, *args, **kwargs):
        from .main import Value
        assert isinstance(val, Value)

        if not isinstance(input, Value):
            # Only assume units if self is not unitless
            if conversions.can_convert(val.units):
                input = Value(float(input), None)
            else:
                warnings.warn(f"The input was not a Value object. Assuming units are {val.units}")
                input = Value(float(input), val.units)
        return f(val, input, *args, **kwargs)
    
    return wrapper

def force_unitless(f):
    """A decorator to try to force a Value object to be
    unitless (if the units of the object can be converted
    to unitless). Otherwise warns the user that the Value
    object is not unitless. The Value returned by the 
    function will be unitless regardless of the input units.

    This decorator is for taking the log or exponent of a Value
    (or a similar function). These functions are typically only
    used on unitless values. If you use one of these functions
    on a Value with units, then the resulting units would be
    meaningless, so it simply returns a unitless Value.
    """
    def wrapper(val):
        from .main import Value, Units
        assert isinstance(val, Value)

        if conversions.can_convert(val.units):
            val = val.to(None)
        else:
            warnings.warn(f"Function '{f.__name__}' expects a unitless number. "
                          f"The supplied Value has units of {val.units}")

        new_val: Value = f(val)

        # Force the output units to be unitless
        new_val.units = Units(None)

        return new_val
    
    return wrapper