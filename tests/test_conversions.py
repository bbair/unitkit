import unittest
from unitkit import conversions, Units

class TestConversions(unittest.TestCase):

    def test_volumes(self):
        m3 = Units("m^3")
        L = Units("L")
        self.assertTrue(conversions.can_convert(m3 / L))

    def test_complex_conversions(self):
        units1 = Units("L*atm/mol/K")
        units2 = Units("J/mol/K")
        self.assertTrue(conversions.can_convert(units1 / units2))

        units1 = Units("W/m2/K")
        units2 = Units("J/min/in2/K")
        self.assertTrue(conversions.can_convert(units1 / units2))


if __name__ == "__main__":
    unittest.main()