from .baseUnit import BaseUnit, Custom, Dimension

from .amount import Amount
from .charge import Charge
from .current import Current
from .energy import Energy
from .force import Force
from .frequency import Frequency
from .length import Length
from .mass import Mass
from .power import Power
from .pressure import Pressure
from .temperature import Temperature
from .time import Time
from .viscosity import Viscosity
from .voltage import Voltage
from .volume import Volume

all_dimensions: list[Dimension] = [
    Amount,
    Charge,
    Current,
    Energy,
    Force,
    Frequency,
    Mass,
    Power,
    Pressure,
    Temperature,
    Time,
    Viscosity,
    Voltage,
    Volume,
    Length, # Length goes after time so "min" doesn't get interpreted as a milli-inch
]

all_base_units = []
for dim in all_dimensions:
    all_base_units.extend(dim().units)