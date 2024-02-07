# unitkit
A python package for handling units and unit conversions.

# Usage

```Python
>>> from unitkit import Value

# Create a "Value" object (a number with units)
>>> my_value = Value(5, "kJ/kg")

# Convert to new units
>>> my_value.convert_units("BTU/lbm")
Value(2.1496153532127984, 'BTU lbm^-1')

# Convert using a molecular weight
>>> molecular_weight = Value(10, "g/mol")
>>> my_value.convert_units("kJ/mol", molecular_weight)
Value(0.05, 'kJ mol^-1')

# Add, subtract, multiply, or divide "Value" objects
>>> my_value2 = Value(3000, "J/kg")
>>> my_value + my_value2
Value(8.0, 'kJ kg^-1')

>>> mass = Value(10, "kg")
>>> acceleration = Value(5, "m/s^2")
>>> force = mass * acceleration
>>> force
Value(50.0, 'kg m s^-2')
```
