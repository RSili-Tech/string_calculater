import re
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
    # if len(numbers) > 1 :
      
    #     int_array = [int(numeric_string) for numeric_string in numbers]
        
            
    #     return sum(int_array)
    # else :
    #     return string

def check_newline_and_comma_seperated_numbers(string):
    
    numbers         = []    
    string_array    = refecter_string(string)
    print(string_array)
    for number in string_array : 
        if number.isnumeric():
            numbers.append(chr)
        elif number.isdigit(): 
            validate_numbers_for_negative_value(number)

    print(numbers)
    # # print(numbers)
    # # number_count    = len(numbers)
    # # if number_count > 0 :
    # #     return numbers    
    # # else :
    # #     return False

def validate_numbers_for_negative_value(number):    
    if int(number) < 0 :
        raise ValueError
        
def refecter_string(string):
    
    res = re.findall('[-+]?\d+', string)
    return res