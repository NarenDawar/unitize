import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from convertly.volume import VolumeConverter  

class TestVolumeConverter(unittest.TestCase):
    def test_liters_to_gallons(self):
        self.assertAlmostEqual(VolumeConverter.convert(1, 'liters', 'gallons'), 0.264172, places=5)

    def test_cubic_meters_to_liters(self):
        self.assertAlmostEqual(VolumeConverter.convert(1, 'cubic_meters', 'liters'), 1000.0, places=5)

    def test_milliliters_to_cubic_centimeters(self):
        self.assertAlmostEqual(VolumeConverter.convert(100, 'milliliters', 'cubic_centimeters'), 100.0, places=5)

    def test_cubic_inches_to_cubic_feet(self):
        self.assertAlmostEqual(VolumeConverter.convert(1728, 'cubic_inches', 'cubic_feet'), 1.0, places=5)

    def test_pints_to_quarts(self):
        self.assertAlmostEqual(VolumeConverter.convert(2, 'pints', 'quarts'), 1.0, places=5)

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            VolumeConverter.convert('invalid', 'liters', 'gallons')

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            VolumeConverter.convert(1, 'invalid_unit', 'gallons')

    def test_invalid_to_unit(self):
        with self.assertRaises(ValueError):
            VolumeConverter.convert(1, 'liters', 'invalid_unit')

if __name__ == '__main__':
    unittest.main()
