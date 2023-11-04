from .baseUnit import BaseUnit, Custom, Dimension

from .amount import Amount
from .charge import Charge
from .energy import Energy
from .force import Force
from .frequency import Frequency
from .length import Length
from .mass import Mass
from .power import Power
from .pressure import Pressure
from .temperature import Temperature
from .time import Time
from .volume import Volume

all_dimensions: list[Dimension] = [
    Amount,
    Charge,
    Energy,
    Force,
    Frequency,
    Length,
    Mass,
    Power,
    Pressure,
    Temperature,
    Time,
    Volume
]

all_base_units = []
for dim in all_dimensions:
    all_base_units.extend(dim().units)