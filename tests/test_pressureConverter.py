import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from convertly.pressure import PressureConverter

class TestPressureConverter(unittest.TestCase):
    def test_pascals_to_kilopascals(self):
        self.assertAlmostEqual(PressureConverter.convert(1000, 'pascals', 'kilopascals'), 1.0, places=5)

    def test_psi_to_bar(self):
        self.assertAlmostEqual(PressureConverter.convert(14.5038, 'psi', 'bar'), 1.0, places=5)

    def test_atmospheres_to_pascals(self):
        self.assertAlmostEqual(PressureConverter.convert(1, 'atmospheres', 'pascals'), 101325.0, places=1)

    def test_bar_to_psi(self):
        self.assertAlmostEqual(PressureConverter.convert(1, 'bar', 'psi'), 14.5038, places=5)

    def test_kilopascals_to_atmospheres(self):
        self.assertAlmostEqual(PressureConverter.convert(101.325, 'kilopascals', 'atmospheres'), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
