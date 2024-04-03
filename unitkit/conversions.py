def convert(val, new_units, mw = None):
    from .main import Value, Units
    assert isinstance(val, Value)

    if not isinstance(new_units, Units):
        new_units = Units(new_units)

    # Check if its just converting between two temperature units
    if is_temperature_conversion(val.units, new_units):

        if not can_convert(val.units / new_units):
            raise Exception(f"Unable to convert temperature from {val.units} to {new_units}")    
        
        converter = get_temperature_converter(val.units, new_units)
        new = Value(converter(val.value), new_units, val.sigfigs)
        return new

    converter_units: Units = new_units / val.units

    if converter_units.is_unitless():
        return Value(val.value, new_units, val.sigfigs)

    needs_mw = False
    if not can_convert(converter_units):
        mw_units = Units("g/mol")
        if can_convert(converter_units * mw_units):
            if mw is None:
                raise Exception(f"Needs the molecular weight to convert but no molecular weight was provided.")
            needs_mw = True
            mw = 1 / mw
        elif can_convert(converter_units / mw_units):
            if mw is None:
                raise Exception(f"Needs the molecular weight to convert but no molecular weight was provided.")
            needs_mw = True
        else:
            raise Exception(f"The units ({val.units}) can't be converted to the new units ({new_units})")

    conversion_factor = build_conversion_factor(converter_units, mw, needs_mw)
    new = val * conversion_factor
    new.units = new_units
    new.sigfigs = val.sigfigs
    return new

def can_convert(units):
    return _can_convert(units.base_units)

def _can_convert(units):
    dimensions = {}
    for u in units:
        if not u.dimension in dimensions:
            dimensions[u.dimension] = 0
        dimensions[u.dimension] += u.exp
    if all(v == 0 for v in dimensions.values()):
        return True
    return try_expanded(units)


def try_expanded(units):
    tried = []
    remaining: list = units.copy()
    while len(remaining) > 0:
        current = remaining.pop()
        current_dbase, _ = current.to_dimension_base()
        if current_dbase.can_expand():
            if _can_convert(tried + current_dbase.expand().base_units + remaining):
                return True
        tried.append(current)
    return False


def build_conversion_factor(converter_units, mw, needs_mw):
    from .main import Value
    factor = Value(1, None)
    
    if needs_mw:
        converter_units /= mw.units
        factor *= mw

    converter_units, modifier = converter_units.expand_all()
    factor *= modifier

    for u in converter_units.base_units:
        factor *= Value(u._mod(), u)
    return factor


def is_temperature_conversion(old_units, new_units):
    from .base import Temperature

    # Each set of units has to just be made of a single temperature base unit
    if len(old_units.base_units) == 1 and len(new_units.base_units) == 1:
        old, new = old_units.base_units[0], new_units.base_units[0]

        return old.dimension == Temperature and new.dimension == Temperature
    
    return False


def get_temperature_converter(old_units, new_units):
    from .main import Units
    assert isinstance(old_units, Units)
    assert isinstance(new_units, Units)

    def converter(T):
        unit1 = old_units.base_units[0]
        T = T ** unit1.exp
        T = (T + unit1.shift_modifier) / unit1.base_modifier

        unit2 = new_units.base_units[0]
        T = T * unit2.base_modifier - unit2.shift_modifier
        T = T ** unit2.exp
        return T
    return converter