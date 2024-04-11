import unittest
from unitkit.main import Value

class TestMain(unittest.TestCase):

    def test_volumes(self):
        m3 = Value(15, "m^3")
        L = m3.to("L")
        self.assertEqual(L, Value(15000, "L"))

        gal = L.to("gal")
        self.assertEqual(gal, Value(3963.0118890357, "gal"))

        gal2 = m3.to("gal")
        self.assertEqual(gal, gal2)

    def test_viscosity(self):
        P = Value(10, "P")
        Pa_s = P.to("Pa*s")
        self.assertEqual(Pa_s, Value(1, "Pa*s"))

    def test_simplify(self):
        value = Value(1, "in/m")
        self.assertEqual(value.simplify_units(), value.to(None))

        value = Value(1, "m3/gal*Pa")
        self.assertEqual(value.simplify_units(), value.to("Pa"))

if __name__ == "__main___":
    unittest.main()