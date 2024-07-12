class SpeedConverter:
    conversion_factors = {
        'meters_per_second': 1.0,
        'kilometers_per_hour': 3.6,
        'miles_per_hour': 2.23694,
        'feet_per_second': 3.28084,
        'knots': 1.94384
    }

    @staticmethod
    def convert(value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise ValueError("Invalid value. Not an integer or float.")
        
        if from_unit.lower() not in SpeedConverter.conversion_factors or to_unit.lower() not in SpeedConverter.conversion_factors:
            raise ValueError("Invalid unit. Not a real unit or unit is not supported. Please use a more standard metric.")
        
        comp_value = value / SpeedConverter.conversion_factors[from_unit.lower()]
        final_value = comp_value * SpeedConverter.conversion_factors[to_unit.lower()]
        return final_value
