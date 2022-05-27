
import numbers
from pickle import FALSE


def Add(param):
    if param == "":
        return 0
    #check for comma seperate numbers in string
    else:
       
        number = param.split(' ')
        

    return param
  
def add_string_numbers(string):
    numbers                 = []
    comma_seperated_numbers = check_comma_seperated_numbers(string)
    space_seperated_numbers = check_space_seperated_numbers(string)

    if(comma_seperated_numbers):
        numbers = comma_seperated_numbers

    elif space_seperated_numbers:
        numbers = space_seperated_numbers

def check_comma_seperated_numbers(string):
    numbers         = string.split(',')
    number_count    = len(numbers)
    if(number_count>1):
        return numbers
    else :
        return FALSE


def check_space_seperated_numbers(string):
    numbers         = string.split(' ')
    number_count    = len(numbers)
    if(number_count>1):
        return numbers
    else :
        return FALSE

def check_newline_seperated_numbers(string):
    numbers         = string.split('\n')
    number_count    = len(numbers)
    if(number_count>1):
        return numbers
    else :
        return FALSE

def validate_numbers_for_negative_value(numbers):
    if any(number < 0 for number in numbers):
        raise ValueError