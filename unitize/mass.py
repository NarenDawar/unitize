class MassConverter:
    conversion_factors = {
        'grams': 1.0,
        'kilograms': 0.001,
        'milligrams': 1000.0,
        'pounds': 0.00220462,
        'ounces': 0.035274
    }

    def add_custom_unit(unit_name, conversion_factor):
        MassConverter.conversion_factors[unit_name.lower()] = conversion_factor

    @staticmethod
    def convert(value, from_unit, to_unit):

        if(not isinstance(value, int) and not isinstance(value, float)):
            raise ValueError("Invalid value. Not an integer or float. ")
        
        if from_unit.lower() not in MassConverter.conversion_factors or to_unit.lower() not in MassConverter.conversion_factors:
            raise ValueError("Invalid unit. Not a real unit or unit is not supported. Please use a more standard metric.")
        
        comp_value = value / MassConverter.conversion_factors[from_unit.lower()]
        final_value = comp_value * MassConverter.conversion_factors[to_unit.lower()]
        return final_value