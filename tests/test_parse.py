import unittest
from unitkit import parse, base, Units
class TestParse(unittest.TestCase):

    def test_time(self):
        minutes = Units("min")
        self.assertEqual(len(minutes.base_units), 1)
        self.assertIsInstance(minutes.base_units[0], base.time.minute)


if __name__ == "__main__":
    unittest.main()