Usage
=====

Here's how to use unitize to convert units.

Length Conversion
-----------------

.. code-block:: python

    from unitize.length import LengthConverter

    # Convert 1000 meters to kilometers
    kilometers = LengthConverter.convert(1000, 'meters', 'kilometers')
    print(kilometers)  # Output: 1.0

Mass Conversion
---------------

.. code-block:: python

    from unitize.mass import MassConverter

    # Convert 1000 grams to kilograms
    kilograms = MassConverter.convert(1000, 'grams', 'kilograms')
    print(kilograms)  # Output: 1.0

Time Conversion
---------------

.. code-block:: python

    from unitize.time import TimeConverter

    # Convert 3600 seconds to hours
    hours = TimeConverter.convert(3600, 'seconds', 'hours')
    print(hours)  # Output: 1.0

Temperature Conversion
----------------------

.. code-block:: python

    from unitize.temperature import TemperatureConverter

    # Convert 100 degrees Celsius to Fahrenheit
    fahrenheit = TemperatureConverter.convert(100, 'celsius', 'fahrenheit')
    print(fahrenheit)  # Output: 212.0

Volume Conversion
-----------------

.. code-block:: python

    from unitize.volume import VolumeConverter

    # Convert 1 liter to milliliters
    milliliters = VolumeConverter.convert(1, 'liters', 'milliliters')
    print(milliliters)  # Output: 1000.0

Speed Conversion
----------------

.. code-block:: python

    from unitize.speed import SpeedConverter

    # Convert 1 meter per second to kilometers per hour
    kilometers_per_hour = SpeedConverter.convert(1, 'meters_per_second', 'kilometers_per_hour')
    print(kilometers_per_hour)  # Output: 3.6

    # Convert 1 mile per hour to knots
    knots = SpeedConverter.convert(1, 'miles_per_hour', 'knots')
    print(knots)  # Output: 0.868976

Pressure Conversion
-------------------

.. code-block:: python

    from unitize.pressure import PressureConverter

    # Convert 1000 pascals to kilopascals
    kilopascals = PressureConverter.convert(1000, 'pascals', 'kilopascals')
    print(kilopascals)  # Output: 1.0

    # Convert 1 atmosphere to pascals
    pascals = PressureConverter.convert(1, 'atmospheres', 'pascals')
    print(pascals)  # Output: 101325.0
