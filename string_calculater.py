
import numbers
from pickle import FALSE


def Add(param):
    if param == "": return 0
    #check for comma seperate numbers in string
    else:
       sum = add_string_numbers(param)       
       return sum

def add_string_numbers(string):
    numbers                     = []
    numbers   = check_newline_and_comma_seperated_numbers(string)   
    if len(numbers) > 1 :
        check_negative_numbers(numbers) 
        int_array = [int(numeric_string) for numeric_string in numbers]
        validate_numbers_for_negative_value(int_array)   
            
        return sum(int_array)
    else :
        return string

def check_newline_and_comma_seperated_numbers(string):
    string          = string.replace('\n', ',')  
    string          = string.replace(' ', ',')   
    numbers         = string.split(',')    
    number_count    = len(numbers)
    if number_count > 0 :
        return numbers    
    else :
        return False

def validate_numbers_for_negative_value(numbers):
    if any( int(number) < 0 for number in numbers):
        raise ValueError

def check_negative_numbers(numbers):
    negative_numbers = filter(lambda x: x < 0, numbers)
    print(negative_numbers)
    if negative_numbers : 
        raise Exception('negatives not allowed ')