class FrequencyConverter:
    conversion_factors = {
        'hertz': 1.0,
        'kilohertz': 1 / 1000.0,
        'megahertz': 1 / 1000000.0,
        'gigahertz': 1 / 1000000000.0
    }

    @staticmethod
    def convert(value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise ValueError("Invalid value. Not an integer or float.")
        if from_unit.lower() not in FrequencyConverter.conversion_factors or to_unit.lower() not in FrequencyConverter.conversion_factors:
            raise ValueError("Invalid unit. Not a real unit or unit is not supported. Please use a more standard metric.")
        
        comp_value = value / FrequencyConverter.conversion_factors[from_unit.lower()]
        final_value = comp_value * FrequencyConverter.conversion_factors[to_unit.lower()]
        return final_value
