import unittest
from unitkit import parse, base, Units
class TestParse(unittest.TestCase):

    def test_time(self):
        minutes = Units("min")
        self.assertEqual(len(minutes.base_units), 1)
        self.assertIsInstance(minutes.base_units[0], base.time.minute)
        self.assertEqual(minutes.base_units[0].exp, 1)

    def test_viscosity(self):
        cP = Units("cP")
        self.assertEqual(len(cP.base_units), 1)
        self.assertIsInstance(cP.base_units[0], base.viscosity.poise)
        self.assertEqual(cP.base_units[0].exp, 1)

    def test_python_exponent(self):
        lcp = Units("J mol**-1 K**-1")
        self.assertEqual(len(lcp.base_units), 3)

        # Check the J portion
        self.assertIsInstance(lcp.base_units[0], base.energy.joule)
        self.assertEqual(lcp.base_units[0].exp, 1)

        # Check the mol portion
        self.assertIsInstance(lcp.base_units[1], base.amount.mol)
        self.assertEqual(lcp.base_units[1].exp, -1)

        # Check the K portion
        self.assertIsInstance(lcp.base_units[2], base.temperature.kelvin)
        self.assertEqual(lcp.base_units[2].exp, -1)

    
    def test_complex(self):
        solp = Units("(J/m3)^(1/2)")
        self.assertEqual(len(solp.base_units), 2)
        
        # Check the J portion
        self.assertIsInstance(solp.base_units[0], base.energy.joule)
        self.assertEqual(solp.base_units[0].exp, 0.5)

        # Check the m portion
        self.assertIsInstance(solp.base_units[1], base.length.meter)
        self.assertEqual(solp.base_units[1].exp, -1.5)

if __name__ == "__main__":
    unittest.main()