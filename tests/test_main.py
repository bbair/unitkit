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

if __name__ == "__main___":
    unittest.main()