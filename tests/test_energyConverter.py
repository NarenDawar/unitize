import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unitize.energy import EnergyConverter

class TestEnergyConverter(unittest.TestCase):
    def test_joules_to_calories(self):
        self.assertAlmostEqual(EnergyConverter.convert(1000, 'joules', 'calories'), 239.006, places=5)

    def test_calories_to_joules(self):
        self.assertAlmostEqual(EnergyConverter.convert(1, 'calories', 'joules'), 4.184, places=5)

    def test_joules_to_kilowatt_hours(self):
        self.assertAlmostEqual(EnergyConverter.convert(3600000, 'joules', 'kilowatt_hours'), 1.0, places=5)

    def test_BTU_to_joules(self):
        self.assertAlmostEqual(EnergyConverter.convert(1, 'BTU', 'joules'), 1055.06, places=2)

if __name__ == '__main__':
    unittest.main()
