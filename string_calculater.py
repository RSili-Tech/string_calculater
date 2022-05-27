
import numbers
from pickle import FALSE


def Add(param):
    if param == "": return 0
    #check for comma seperate numbers in string
    else:
        sum = add_string_numbers(param)
        if int(sum) > 0 :
            return sum
        else :
            return 'Unable to calculate'

    
  
def add_string_numbers(string):
    numbers                     = []
    comma_seperated_numbers     = check_comma_seperated_numbers(string)
    space_seperated_numbers     = check_space_seperated_numbers(string)
    newline_seperated_numbers   = check_newline_seperated_numbers(string)

    if comma_seperated_numbers :
        numbers = comma_seperated_numbers

    elif space_seperated_numbers:
        numbers = space_seperated_numbers
    
    elif newline_seperated_numbers:
        numbers = space_seperated_numbers

    if len(numbers) > 1 :
        validate_numbers_for_negative_value(numbers)
        int_array = [int(numeric_string) for numeric_string in numbers]
        return sum(int_array)
    else :
        return string



def check_comma_seperated_numbers(string):
    numbers         = string.split(',')
    number_count    = len(numbers)
    if number_count > 1 :
        return numbers   
    else :
        return False


def check_space_seperated_numbers(string):
    numbers         = string.split(' ')
    number_count    = len(numbers)
    if number_count > 0 :
        return numbers    
    else :
        return False

def check_newline_seperated_numbers(string):
    numbers         = string.split('\n')
    number_count    = len(numbers)
    if number_count > 0 :
        return numbers    
    else :
        return False

def validate_numbers_for_negative_value(numbers):
    if any( int(number) < 0 for number in numbers):
        raise ValueError