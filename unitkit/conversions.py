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
        return (old_units.base_units[0].dimension == Temperature and
                new_units.base_units[0].dimension == Temperature)
    return False


def get_temperature_converter(old_units, new_units):
    def converter(T):
        unit1 = old_units.base_units[0]
        T = (T + unit1.shift_modifier) / unit1.base_modifier

        unit2 = new_units.base_units[0]
        T = T * unit2.base_modifier - unit2.shift_modifier
        return T
    return converter