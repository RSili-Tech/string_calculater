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
   
    test_str = "gfg + 4-1i,s + 5best-18 1\n2,3"
    res = re.findall('[-+]?\d+', test_str)
  
    print("The split string is : " + str(res)) 
    # numbers         = []
    # char_position   = False
   
    # for index, chr in enumerate(string, start=0): 
    #     next_position  = index+1
    #     next_char      = string[next_position]
    #     # if index > 0 :
    #     #     prev_position  = int(index-1)
    #     #     prev_char      = string[prev_position]
    #     # else :
    #     #     prev_position  = 0
    #     #     prev_char      = ''

        
     
    #     if chr == '-' and  next_char.isdigit():  
    #         print("next Position " + str(index ) + ' value: '+ next_char )
    #        # print ('Negative')
    # #        # validate_numbers_for_negative_value(next_char)
    # #        print ('negative ')
    # #     elif chr.isdigit() and prev_char != '-':                                      
    # #             numbers.append(chr)
            
    # # print(numbers)
    # # number_count    = len(numbers)
    # # if number_count > 0 :
    # #     return numbers    
    # # else :
    # #     return False

def validate_numbers_for_negative_value(number):
    number = -number
    if int(number) < 0 :
        raise ValueError
