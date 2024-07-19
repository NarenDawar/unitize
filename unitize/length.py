from history import *

class LengthConverter:
    conversion_factors = {
        'meters': (1.0),
        'kilometers': (0.001),
        'centimeters': (100.0),
        'millimeters': (1000.0),
        'inches': (39.3701),
        'feet': (3.28084),
        'yards': (1.09361),
        'miles': (0.000621371)
    }

    def add_custom_unit(unit_name, conversion_factor):
        LengthConverter.conversion_factors[unit_name.lower()] = conversion_factor

    @staticmethod
    def convert(value, from_unit, to_unit):

        if(not isinstance(value, (int, float))):
            raise ValueError("Invalid value. Not an integer or float. ")
        if from_unit.lower() not in LengthConverter.conversion_factors or to_unit.lower() not in LengthConverter.conversion_factors:
            raise ValueError("Invalid unit. Not a real unit or unit is not supported. Please use a more standard metric.")
        
        comp_value = (value) / LengthConverter.conversion_factors[from_unit.lower()]
        final_value = comp_value * LengthConverter.conversion_factors[to_unit.lower()]

        conversion = {
            'value': value,
            'from_unit': from_unit,
            'to_unit': to_unit,
            'result': final_value
        }
        add_to_history(conversion)

        return (final_value)