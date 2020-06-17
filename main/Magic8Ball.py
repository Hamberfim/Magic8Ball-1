"""
Program: this_file_name.py
Author:  Firstname Lastname
Date: MM/DD/YYYY

Change this description to be more relevant.
This program creates a function that prints 'Hello World'
as output.  The function is then called.
"""

import random
from main import constants

def get_random_number():
    """
    Use reST style.

    :param parameter_1: this is what the first parameter represents
    :param parameter_2: this is what the second parameter represents
    :returns: this is what is returned
    :raises keyError: raises an exception
    """
    randomized_number = random.randint(0,19)
    return randomized_number

def convert_number_to_text(input_number):
    """
    Use reST style.

    :param parameter_1: this is what the first parameter represents
    :param parameter_2: this is what the second parameter represents
    :returns: this is what is returned
    :raises keyError: raises an exception
    """
    try:
        input_number = int(input_number)
    except:
        raise ValueError
    if 0 <= input_number <= 19:
        return constants.Eight_Ball_Responses[input_number]
    else:
        raise ValueError

def main_loop():
    """
    Use reST style.

    :param parameter_1: this is what the first parameter represents
    :param parameter_2: this is what the second parameter represents
    :returns: this is what is returned
    :raises keyError: raises an exception
    """
    pass

    #sentinal value = true
    #let user ask a question
        #randomly pick from 20 answers
    #print answer
    #let user ask another question
    #if user typed in 'exit' stop program


if __name__ == '__main__':
    main_loop()
