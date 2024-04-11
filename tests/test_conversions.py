import unittest
from unitkit import conversions, Units, Value

class TestConversions(unittest.TestCase):

    def test_volumes(self):
        m3 = Units("m^3")
        L = Units("L")
        self.assertTrue(conversions.can_convert(m3 / L))

    def test_viscosity(self):
        cP = Units("cP")
        pas = Units("Pa*s")
        self.assertTrue(conversions.can_convert(cP / pas))

    def test_complex_conversions(self):
        units1 = Units("L*atm/mol/K")
        units2 = Units("J/mol/K")
        self.assertTrue(conversions.can_convert(units1 / units2))

        units1 = Units("W/m2/K")
        units2 = Units("J/min/in2/K")
        self.assertTrue(conversions.can_convert(units1 / units2))


class TestTemperatureConversions(unittest.TestCase):

    def test_direct(self):
        t1 = Units("K")
        t2 = Units("degC")
        self.assertTrue(conversions.can_convert(t1 / t2))

    def test_can_inverse(self):
        t1 = Units("1/K")
        t2 = Units("1/degC")
        self.assertTrue(conversions.can_convert(t1 / t2))

    def test_degC_to_K(self):
        t1 = Value(15, "degC")
        t2 = Value(288.15, "K")
        self.assertEqual(conversions.convert(t1, "K"), t2)

    def test_degC_to_K_inverse(self):
        t1 = 1 / Value(15, "degC")
        t2 = 1 / Value(288.15, "K")
        self.assertEqual(conversions.convert(t1, "1/K"), t2)

    def test_degR_to_K_inverse(self):
        t1 = 1 / Value(480, "degR")
        t2 = 1 / Value(480 * 5 / 9, "K")
        self.assertEqual(conversions.convert(t1, "1/K"), t2)

    def test_complex(self):
        lcp1 = Value(4.18, "J/g/K")
        lcp2 = Value(4.18, "J/g/degC")
        self.assertEqual(lcp1.to("J/g/degC"), lcp2)


if __name__ == "__main__":
    unittest.main()