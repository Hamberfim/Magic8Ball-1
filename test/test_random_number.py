
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

    def test_return_value_type(self):
        #assertEqual( parameter1, parameter2)
            ## parameter1 == parameter2
        #assertEqual( "Expected Value or outcome", function_call(param3))
        self.assertEqual(type(1), type(m8b.get_random_number()))
    def test_return_greater_than_0(self):
        self.assertGreater(m8b.get_random_number(),0) # a > b
    def test_return_less_than_20(self):
        self.assertGreater(20,m8b.get_random_number())

if __name__ == '__main__':
    unittest.main()
