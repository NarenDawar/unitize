import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unitwise.speed import SpeedConverter

class TestSpeedConverter(unittest.TestCase):
    def test_mps_to_kph(self):
        self.assertAlmostEqual(SpeedConverter.convert(1, 'meters_per_second', 'kilometers_per_hour'), 3.6, places=5)

    def test_mph_to_knots(self):
        self.assertAlmostEqual(SpeedConverter.convert(1, 'miles_per_hour', 'knots'), 0.868976, places=5)

    def test_knots_to_fps(self):
        self.assertAlmostEqual(SpeedConverter.convert(1, 'knots', 'feet_per_second'), 1.68781, places=5)

    def test_kph_to_mph(self):
        self.assertAlmostEqual(SpeedConverter.convert(100, 'kilometers_per_hour', 'miles_per_hour'), 62.1371, places=3)

    def test_fps_to_mps(self):
        self.assertAlmostEqual(SpeedConverter.convert(10, 'feet_per_second', 'meters_per_second'), 3.048, places=5)

if __name__ == '__main__':
    unittest.main()
