Usage
=====

Here's how to use UnitWise to convert units.

Length Conversion
-----------------

.. code-block:: python

    from UnitWise.length import LengthConverter

    # Convert 1000 meters to kilometers
    kilometers = LengthConverter.convert(1000, 'meters', 'kilometers')
    print(kilometers)  # Output: 1.0

Mass Conversion
---------------

.. code-block:: python

    from UnitWise.mass import MassConverter

    # Convert 1000 grams to kilograms
    kilograms = MassConverter.convert(1000, 'grams', 'kilograms')
    print(kilograms)  # Output: 1.0

Time Conversion
---------------

.. code-block:: python

    from UnitWise.time import TimeConverter

    # Convert 3600 seconds to hours
    hours = TimeConverter.convert(3600, 'seconds', 'hours')
    print(hours)  # Output: 1.0

Temperature Conversion
----------------------

.. code-block:: python

    from UnitWise.temperature import TemperatureConverter

    # Convert 100 degrees Celsius to Fahrenheit
    fahrenheit = TemperatureConverter.convert(100, 'celsius', 'fahrenheit')
    print(fahrenheit)  # Output: 212.0

Volume Conversion
-----------------

.. code-block:: python

    from UnitWise.volume import VolumeConverter

    # Convert 1 liter to milliliters
    milliliters = VolumeConverter.convert(1, 'liters', 'milliliters')
    print(milliliters)  # Output: 1000.0
