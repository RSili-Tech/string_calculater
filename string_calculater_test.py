from unittest import result
import pytest
from string_calculater import stringcalculater

# Good Test Cycle
# Make test fail
# Make test pass
# Refator

def test_stringcalculater_should_return_zero_on_empty_string():
    #setup
    #excersice
    #verify/Validate
    result = stringcalculater("")
    assert result == 0


def test_stringcalculater_should_return_the_same_number():
    #setup
    #excersice
    #verify/Validate
    result = stringcalculater("1")
    assert result == 1