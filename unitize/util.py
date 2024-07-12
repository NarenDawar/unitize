from .length import LengthConverter
from .mass import MassConverter
from .temperature import TemperatureConverter
from .volume import VolumeConverter
from .time import TimeConverter

def convert(value, from_unit, to_unit, category):
    if category == 'length':
        return LengthConverter.convert(value, from_unit, to_unit)
    elif category == 'weight':
        return MassConverter.convert(value, from_unit, to_unit)
    elif category == 'temperature':
        return TemperatureConverter.convert(value, from_unit, to_unit)
    elif category == 'volume':
        return VolumeConverter.convert(value, from_unit, to_unit)
    elif category == 'time':
        return TimeConverter.convert(value, from_unit, to_unit)
    else:
        raise ValueError("Invalid category for conversion. Check documentation if confused.")
