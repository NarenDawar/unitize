import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from convertly.mass import MassConverter  

class TestMassConverter(unittest.TestCase):
    def test_grams_to_kilograms(self):
        self.assertAlmostEqual(MassConverter.convert(1000, 'grams', 'kilograms'), 1.0, places=5)

    def test_ounces_to_pounds(self):
        self.assertAlmostEqual(MassConverter.convert(16, 'ounces', 'pounds'), 1.0, places=5)

    def test_milligrams_to_grams(self):
        self.assertAlmostEqual(MassConverter.convert(1000, 'milligrams', 'grams'), 1.0, places=5)

    def test_pounds_to_ounces(self):
        self.assertAlmostEqual(MassConverter.convert(1, 'pounds', 'ounces'), 16.0, places=4)

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            MassConverter.convert('invalid', 'grams', 'kilograms')

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            MassConverter.convert(1000, 'invalid_unit', 'kilograms')

    def test_invalid_to_unit(self):
        with self.assertRaises(ValueError):
            MassConverter.convert(1000, 'grams', 'invalid_unit')

if __name__ == '__main__':
    unittest.main()