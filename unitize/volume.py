class VolumeConverter:
    conversion_factors = {
        'liters': 1.0,
        'milliliters': 1000.0,
        'cubic_meters': 0.001,
        'cubic_centimeters': 1000.0,
        'cubic_inches': 61.0237,
        'cubic_feet': 0.0353147,
        'gallons': 0.264172,
        'quarts': 1.05669,
        'pints': 2.11338,
        'cups': 4.22675
    }

    def add_custom_unit(unit_name, conversion_factor):
        VolumeConverter.conversion_factors[unit_name.lower()] = conversion_factor

    @staticmethod
    def convert(value, from_unit, to_unit):
        if(not isinstance(value, int) and not isinstance(value, float)):
            raise ValueError("Invalid value. Not an integer or float. ")
        if from_unit.lower() not in VolumeConverter.conversion_factors or to_unit.lower() not in VolumeConverter.conversion_factors:
            raise ValueError("Invalid unit. Not a real unit or unit is not supported. Please use a more standard metric.")
        
        comp_value = value / VolumeConverter.conversion_factors[from_unit.lower()]
        final_value = comp_value * VolumeConverter.conversion_factors[to_unit.lower()]
        return final_value