from unittest import result
import pytest
from string_calculater import Add

# Good Test Cycle
# Make test fail
# Make test pass
# Refator

def test_stringcalculater_should_return_zero_on_empty_string():
    #setup
    #excersice
    #verify/Validate
    result = Add("")
    assert result == 0


def test_stringcalculater_should_return_the_same_number_if_input_is_one_number_only():
    #setup
    #excersice
    #verify/Validate
    input = 1
    result = Add(input)
    assert result == input