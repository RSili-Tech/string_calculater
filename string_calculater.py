import re
import pytest
from pickle import FALSE


def Add(param):
    if param == "": return 0
    else:
       sum = add_string_numbers(param)       
       return sum

def add_string_numbers(string):
    numbers                     = []
    numbers   = check_newline_and_comma_seperated_numbers(string)   
    if len(numbers) > 1 :      
        int_array = [int(numeric_string) for numeric_string in numbers]            
        return sum(int_array)
    else :
        return string

def check_newline_and_comma_seperated_numbers(string):
    
    numbers         = []    
    string_array    = refecter_string(string)    
    for number in string_array : 
        if number.isnumeric():
            numbers.append(number)
        elif number.isdigit(): 
            validate_numbers_for_negative_value(number)
    return numbers

def validate_numbers_for_negative_value(number):    
    
    if int(number) < 0 :
        assert pytest.raises(ValueError)

def refecter_string(string):
    
    res = re.findall('[-+]?\d+', string)
    return res