import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from convertly.time import TimeConverter  

class TestTimeConverter(unittest.TestCase):
    def test_seconds_to_minutes(self):
        self.assertAlmostEqual(TimeConverter.convert(60, 'seconds', 'minutes'), 1.0, places=5)

    def test_minutes_to_seconds(self):
        self.assertAlmostEqual(TimeConverter.convert(1, 'minutes', 'seconds'), 60.0, places=5)

    def test_hours_to_minutes(self):
        self.assertAlmostEqual(TimeConverter.convert(1, 'hours', 'minutes'), 60.0, places=5)

    def test_days_to_hours(self):
        self.assertAlmostEqual(TimeConverter.convert(1, 'days', 'hours'), 24.0, places=5)

    def test_weeks_to_days(self):
        self.assertAlmostEqual(TimeConverter.convert(1, 'weeks', 'days'), 7.0, places=5)

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            TimeConverter.convert('invalid', 'seconds', 'minutes')

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            TimeConverter.convert(1, 'invalid_unit', 'minutes')

    def test_invalid_to_unit(self):
        with self.assertRaises(ValueError):
            TimeConverter.convert(1, 'seconds', 'invalid_unit')

if __name__ == '__main__':
    unittest.main()
