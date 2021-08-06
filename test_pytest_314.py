import pytest
from lambdata_madina.helper_functions_oop_312 import Car, inc
import io
import sys


def test_inc():
    """This is a function that tests function inc(x)"""
    assert inc(10) == 11
    assert inc(2) == 5


def test_car():
    """This is a function that tests Car class"""
    test_car = Car('Tesla', 'Cybertruck', 2021, 'Black')
    assert test_car.make == 'Tesla'
    assert test_car.model == 'Cybertruck'
    assert test_car.year == 2021
    assert test_car.color == 'Black'
    assert test_car.mileage == 0

    # Test the print statement of the test_car.drive() function:
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     # Redirect stdout
    test_car.drive()                                # Call function
    sys.stdout = sys.__stdout__                     # Reset redirect
    assert capturedOutput.getvalue() == 'Driving\n' # Now test the captured output
    test_car.set_mileage(300)
    assert test_car.mileage == 300

    # Test the print statement of the test_car.fill_gas() function:
    capturedOutput = io.StringIO()                            # Create StringIO object
    sys.stdout = capturedOutput                               # Redirect stdout
    test_car.fill_gas()                                       # Call function
    sys.stdout = sys.__stdout__                               # Reset redirect
    assert capturedOutput.getvalue() == 'Filling up on gas\n' # Now test the captured output

