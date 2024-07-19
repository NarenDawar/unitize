class TemperatureConverter:
    temps = ["fahrenheit", "celsius", "kelvin"]

    @staticmethod
    def convert(value, from_unit, to_unit):
        if(not isinstance(value, int) and not isinstance(value, float)):
            raise ValueError("Invalid value. Not an integer or float. ")

        
        to_unit_check = to_unit.lower()
        from_unit_check = from_unit.lower()

        if(to_unit_check not in TemperatureConverter.temps or from_unit_check not in TemperatureConverter.temps):
            raise ValueError("Invalid unit. Please use a standard unit for temperature.")

        if from_unit_check == 'celsius':
            if to_unit_check == 'fahrenheit':
                return value * 9/5 + 32
            elif to_unit_check == 'kelvin':
                return value + 273.15
        elif from_unit_check == 'fahrenheit':
            if to_unit_check == 'celsius':
                return (value - 32) * 5/9
            elif to_unit_check == "kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit_check == 'kelvin':
            if to_unit_check == 'celsius':
                return value - 273.15
            elif to_unit_check == 'fahrenheit':
                return (value -  273.15) * 9/5 + 32
        else:
            raise ValueError("Invalid unit. Please use a standard unit for temperature.")
            