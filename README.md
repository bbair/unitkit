# unitkit
This Python package provides functionality for handling calculations involving values with units. It offers classes for defining units, values with units, and performing arithmetic operations on them.

## Installation
The package can be installed directly from GitHub using pip:

```bash
pip install git+https://github.com/abates20/pythonUnits.git
```

## Usage

### Basic Usage
The package is primarily used via the Value object. This object is initialized with a number and a string specifying the units.

```Python
from unitkit import Value
my_value = Value(5, "kJ/kg")
```

Values can be converted to new units with the "convert_units" method or the "to" method for simpler syntax.

```Python
print(my_value.convert_units("BTU/lbm")) # Output: "2.1496153532127984 BTU lbm^-1"
print(my_value.to("BTU/lbm")) # Output: "2.1496153532127984 BTU lbm^-1"
```

### Aritmethic Operations
Value objects can be used in arithmetic expressions (addition, subtraction, multiplication, division, exponentiation, etc.). The package keeps track of the units in the background along the way.

```Python
mass = Value(10, "kg")
acceleration = Value(5, "m/s^2")
force = mass * acceleration
print(force) # Output: "50.0 kg m s^-2"
print(force.to("N")) # Output: "50.0 N"
```

You can mix and match units from different systems (i.e., SI units and imperial units) when doing calculations. Again, the package keeps track of the units in the background.

```Python
rho = Value(50, "lbm/ft3")
mu = Value(0.001, "Pa*s")
v = Value(3, "km/hr")
D = Value(3, "in")
Re = rho * v * D / mu
print(Re) # Output: "450000.0 lbm km in hr^-1 Pa^-1 s^-1 ft^-3"
print(Re.to(None)) # Output: "50858.684950996845 (unitless)"
```

### Additional Features
Some conversions require a molecular weight (e.g., converting from kg to kmol). These conversions can be done by providing a molecular weight as an argument to the "convert_units" and "to" methods.

```Python
molecular_weight = Value(10, "g/mol")
print(my_value.to("kJ/mol", molecular_weight)) # Output: "0.05 kJ mol^-1
```

The package also provides some support for significant figures (sigfigs). Value objects have a roundsf method for rounding based on the number of sigfigs.

```Python
my_value = Value(1.01, "kg")
print(my_value.roundsf(2)) # Output: "1.0 kg"
```
