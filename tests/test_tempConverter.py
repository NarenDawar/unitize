import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unitize.temperature import TemperatureConverter 

class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(TemperatureConverter.convert(100, 'celsius', 'fahrenheit'), 212.0, places=5)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(TemperatureConverter.convert(100, 'celsius', 'kelvin'), 373.15, places=5)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(TemperatureConverter.convert(212, 'fahrenheit', 'celsius'), 100.0, places=5)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(TemperatureConverter.convert(212, 'fahrenheit', 'kelvin'), 373.15, places=5)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(TemperatureConverter.convert(373.15, 'kelvin', 'celsius'), 100.0, places=5)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(TemperatureConverter.convert(373.15, 'kelvin', 'fahrenheit'), 212.0, places=5)

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            TemperatureConverter.convert('invalid', 'celsius', 'fahrenheit')

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            TemperatureConverter.convert(100, 'invalid_unit', 'fahrenheit')

    def test_invalid_to_unit(self):
        with self.assertRaises(ValueError):
            TemperatureConverter.convert(100, 'celsius', 'invalid_unit')

if __name__ == '__main__':
    unittest.main()
