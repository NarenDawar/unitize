import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from convertly.length import LengthConverter

class TestLengthConverter(unittest.TestCase):
    def test_meters_to_kilometers(self):
        self.assertAlmostEqual(LengthConverter.convert(1000, 'meters', 'kilometers'), 1.0, places=5)

    def test_inches_to_feet(self):
        self.assertAlmostEqual(LengthConverter.convert(12, 'inches', 'feet'), 1.0, places=5)

    def test_centimeters_to_meters(self):
        self.assertAlmostEqual(LengthConverter.convert(100, 'centimeters', 'meters'), 1.0, places=5)

    def test_miles_to_yards(self):
        self.assertAlmostEqual(LengthConverter.convert(1, 'miles', 'yards'), 1760, places=2)

    def test_millimeters_to_meters(self):
        self.assertAlmostEqual(LengthConverter.convert(1000, 'millimeters', 'meters'), 1.0, places=5)

    def test_feet_to_inches(self):
        self.assertAlmostEqual(LengthConverter.convert(1, 'feet', 'inches'), 12.0, places=4)

    def test_yards_to_miles(self):
        self.assertAlmostEqual(LengthConverter.convert(1760, 'yards', 'miles'), 1.0, places=5)

    def test_kilometers_to_miles(self):
        self.assertAlmostEqual(LengthConverter.convert(1, 'kilometers', 'miles'), 0.621371, places=5)

    def test_miles_to_kilometers(self):
        self.assertAlmostEqual(LengthConverter.convert(1, 'miles', 'kilometers'), 1.60934, places=5)

if __name__ == '__main__':
    unittest.main()