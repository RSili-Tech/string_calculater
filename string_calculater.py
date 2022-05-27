
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
    if(check_comma_seperated_numbers):
        pass

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
