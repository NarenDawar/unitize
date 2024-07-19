from history import *

class EnergyConverter:
    conversion_factors = {
        'joules': 1.0,
        'calories': 0.239006,
        'kilowatt_hours': 2.77778e-7,
        'btu': 0.000947817
    }

    def add_custom_unit(unit_name, conversion_factor):
        EnergyConverter.conversion_factors[unit_name.lower()] = conversion_factor

    @staticmethod
    def convert(value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise ValueError("Invalid value. Not an integer or float.")
        if from_unit.lower() not in EnergyConverter.conversion_factors or to_unit.lower() not in EnergyConverter.conversion_factors:
            raise ValueError("Invalid unit. Not a real unit or unit is not supported. Please use a more standard metric.")
        
        comp_value = value / EnergyConverter.conversion_factors[from_unit.lower()]
        final_value = comp_value * EnergyConverter.conversion_factors[to_unit.lower()]

        conversion = {
            'value': value,
            'from_unit': from_unit,
            'to_unit': to_unit,
            'result': final_value
        }
        add_to_history(conversion)

        return final_value
