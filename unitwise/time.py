class TimeConverter:
    conversion_factors = {
        'seconds': 1.0,
        'minutes': 1 / 60.0,
        'hours': 1 / 3600.0,
        'days': 1 / 86400.0,
        'weeks': 1 / 604800.0
    }

    @staticmethod
    def convert(value, from_unit, to_unit):

        if(not isinstance(value, int) and not isinstance(value, float)):
            raise ValueError("Invalid value. Not an integer or float. ")
        
        if from_unit.lower() not in TimeConverter.conversion_factors or to_unit.lower() not in TimeConverter.conversion_factors:
            raise ValueError("Invalid unit. Not a real unit or unit is not supported. Please use a more standard metric.")
        
        comp_value = value / TimeConverter.conversion_factors[from_unit.lower()]
        final_value = comp_value * TimeConverter.conversion_factors[to_unit.lower()]
        return final_value