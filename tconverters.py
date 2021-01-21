'''
   Provide functions for temperature conversions
'''

ABSOLUTE_ZERO_CELSIUS = -273.15

def c2f(celsius):
    '''
    Convert a Celsius temperature to Fahrenheit
    :param celsius: the Celsius temperature (float, int, or numeric string)
    :return: The Fahrenheit temperature as a float
    '''
    celsius = float(celsius)
    fahrenheit = 1.8 * celsius + 32

    return fahrenheit

def f2c(fahrenheit):
    '''
    Convert a Fahrenheit temperature to Celsius
    :param fahrenheit: the Fahrenheit temperature (float, int, or numeric string)
    :return: The Celsius temperature as a float
    '''
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * (5/9)

    return celsius

def c2k(celsius):
    """
    Convert Celsius to Kelvin
    :param celsius:  Celsius as float or int
    :return: Kelvin as float
    """
    return celsius - ABSOLUTE_ZERO_CELSIUS

def f2k(fahrenheit):
    return c2k(f2c(fahrenheit))

def k2c(kelvin):
    return kelvin  + (ABSOLUTE_ZERO_CELSIUS)

def k2f(kelvin):
    return c2f(k2c(kelvin))


