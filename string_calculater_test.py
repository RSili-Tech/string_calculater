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
    input = '1'
    result = Add(input)
    assert result == input

def test_stringcalculater_to_add_for_unknowwn_amount_of_number():
    input = '1,2,3'
    result = Add(input)
    assert result 

def test_stringcalculater_to_add_for_newlines_between_number():
    input = "1\n2,3"
    result = Add(input)
    assert result 

def test_stringcalculater_to_show_negative_numbers_not_allowed():    
    input = '-1, -2, -3, 1, 2, 3'   
    assert pytest.raises(ValueError, Add, input)
  