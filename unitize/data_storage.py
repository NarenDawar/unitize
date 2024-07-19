class DataStorageConverter:
    conversion_factors = {
        'bytes': 1.0,
        'kilobytes': 1 / 1024.0,
        'megabytes': 1 / 1048576.0,
        'gigabytes': 1 / 1073741824.0,
        'terabytes': 1 / 1099511627776.0,
        'petabytes': 1 / 1125899906842624.0
    }

    def add_custom_unit(unit_name, conversion_factor):
        DataStorageConverter.conversion_factors[unit_name.lower()] = conversion_factor

    @staticmethod
    def convert(value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise ValueError("Invalid value. Not an integer or float.")
        if from_unit.lower() not in DataStorageConverter.conversion_factors or to_unit.lower() not in DataStorageConverter.conversion_factors:
            raise ValueError("Invalid unit. Not a real unit or unit is not supported. Please use a more standard metric.")
        
        comp_value = value / DataStorageConverter.conversion_factors[from_unit.lower()]
        final_value = comp_value * DataStorageConverter.conversion_factors[to_unit.lower()]
        return final_value
