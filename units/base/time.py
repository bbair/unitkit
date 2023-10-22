from .baseUnit import BaseUnit

class second(BaseUnit):
    
    base = "s"
    dimension = "time"
    __name__ = "second"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class minute(BaseUnit):

    base = "min"
    dimension = "time"
    __name__ = "minute"
    base_modifier = 1 / 60

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class hour(BaseUnit):

    base = "hr"
    dimension = "time"
    __name__ = "hour"
    base_modifier = minute.base_modifier / 60

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class hour2(BaseUnit):

    base = "h"
    dimension = "time"
    __name__ = "hour"
    base_modifier = minute.base_modifier / 60

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class hours(BaseUnit):

    base = "hrs"
    dimension = "time"
    __name__ = "hour"
    base_modifier = minute.base_modifier / 60

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class day(BaseUnit):

    base = "day"
    dimension = "time"
    __name__ = "day"
    base_modifier = hour.base_modifier / 24

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class days(BaseUnit):

    base = "days"
    dimension = "time"
    __name__ = "day"
    base_modifier = hour.base_modifier / 24

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class week(BaseUnit):

    base = "week"
    dimension = "time"
    __name__ = "week"
    base_modifier = day.base_modifier / 7

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class weeks(BaseUnit):

    base = "weeks"
    dimension = "time"
    __name__ = "week"
    base_modifier = day.base_modifier / 7

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class year(BaseUnit):

    base = "yr"
    dimension = "time"
    __name__ = "year"
    base_modifier = day.base_modifier / 365.25

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class year2(BaseUnit):

    base = "year"
    dimension = "time"
    __name__ = "year"
    base_modifier = day.base_modifier / 365.25

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class years(BaseUnit):

    base = "yrs"
    dimension = "time"
    __name__ = "year"
    base_modifier = day.base_modifier / 365.25

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

class years2(BaseUnit):

    base = "years"
    dimension = "time"
    __name__ = "year"
    base_modifier = day.base_modifier / 365.25

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix = prefix, exp = exp)

time_units = [second, minute, hour, hour2, hours, day, days, week, weeks, year, year2, years, years2]