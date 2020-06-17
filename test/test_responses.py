
"""
Program: this_file_name.py
Author:  Firstname Lastname
Date: MM/DD/YYYY
This program tests a function that prints 'Hello World'
as output.  The function is then called.
"""
import unittest
import unittest.mock as mock
from main import Magic8Ball as m8b

class MyTestCase(unittest.TestCase):

    def test_first_response(self):
        #assertEqual( parameter1, parameter2)
            ## parameter1 == parameter2
        #assertEqual( "Expected Value or outcome", function_call(param3))
        self.assertEqual("It is certain.", m8b.convert_number_to_text(0))

    def test_second_response(self):
        self.assertEqual("It is decidedly so.", m8b.convert_number_to_text(1))

if __name__ == '__main__':
    unittest.main()
