import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unitize.data_storage import DataStorageConverter

class TestDataStorageConverter(unittest.TestCase):
    def test_bytes_to_kilobytes(self):
        self.assertAlmostEqual(DataStorageConverter.convert(1024, 'bytes', 'kilobytes'), 1.0, places=5)

    def test_kilobytes_to_megabytes(self):
        self.assertAlmostEqual(DataStorageConverter.convert(1024, 'kilobytes', 'megabytes'), 1.0, places=5)

    def test_megabytes_to_gigabytes(self):
        self.assertAlmostEqual(DataStorageConverter.convert(1024, 'megabytes', 'gigabytes'), 1.0, places=5)

    def test_gigabytes_to_terabytes(self):
        self.assertAlmostEqual(DataStorageConverter.convert(1024, 'gigabytes', 'terabytes'), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
