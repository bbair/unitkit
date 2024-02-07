from .baseUnit import BaseUnit, Dimension

class Time(Dimension):

    __name__ = "Time"

    def __init__(self):
        self.units = [second, minute, hour, hour2, hours, day, days, week, weeks, year, year2, years, years2]
        self.base = second

class second(BaseUnit):
    
    base = "s"
    __name__ = "second"

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())

class minute(BaseUnit):

    base = "min"
    __name__ = "minute"
    base_modifier = 1 / 60

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())

class hour(BaseUnit):

    base = "hr"
    __name__ = "hour"
    base_modifier = minute.base_modifier / 60

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())

class hour2(BaseUnit):

    base = "h"
    __name__ = "hour"
    base_modifier = hour.base_modifier

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())

class hours(BaseUnit):

    base = "hrs"
    __name__ = "hour"
    base_modifier = hour.base_modifier

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())

class day(BaseUnit):

    base = "day"
    __name__ = "day"
    base_modifier = hour.base_modifier / 24

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())

class days(BaseUnit):

    base = "days"
    __name__ = "day"
    base_modifier = day.base_modifier

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())

class week(BaseUnit):

    base = "week"
    __name__ = "week"
    base_modifier = day.base_modifier / 7

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())

class weeks(BaseUnit):

    base = "weeks"
    __name__ = "week"
    base_modifier = week.base_modifier

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())

class year(BaseUnit):

    base = "yr"
    __name__ = "year"
    base_modifier = day.base_modifier / 365.25

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())

class year2(BaseUnit):

    base = "year"
    __name__ = "year"
    base_modifier = year.base_modifier

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())

class years(BaseUnit):

    base = "yrs"
    __name__ = "year"
    base_modifier = year.base_modifier

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())

class years2(BaseUnit):

    base = "years"
    __name__ = "year"
    base_modifier = year.base_modifier

    def __init__(self, prefix = "", exp = 1):
        super().__init__(prefix=prefix, exp=exp, dimension=Time())