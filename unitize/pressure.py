class PressureConverter:
    conversion_factors = {
        'pascals': 1.0,
        'kilopascals': 0.001,
        'bar': 1e-5,
        'psi': 0.000145038,
        'atmospheres': 9.86923e-6
    }

    def add_custom_unit(unit_name, conversion_factor):
        PressureConverter.conversion_factors[unit_name.lower()] = conversion_factor

    @staticmethod
    def convert(value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise ValueError("Invalid value. Not an integer or float.")
        
        if from_unit.lower() not in PressureConverter.conversion_factors or to_unit.lower() not in PressureConverter.conversion_factors:
            raise ValueError("Invalid unit. Not a real unit or unit is not supported. Please use a more standard metric.")
        
        comp_value = value / PressureConverter.conversion_factors[from_unit.lower()]
        final_value = comp_value * PressureConverter.conversion_factors[to_unit.lower()]
        return final_value
