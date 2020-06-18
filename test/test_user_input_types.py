"""
Program: this_file_name.py
Author:  Firstname Lastname
Date: MM/DD/YYYY

This program tests a function that prints 'Hello World'
as output.  The function is then called.
"""
import unittest
import unittest.mock as mock
from unittest.mock import patch
from main import user_input_types as uit

class MyTestCase(unittest.TestCase):

    def test_basic_function(self):
        self.assertEqual(uit.a_function_with_no_parameters_or_input(), 5)

    def test_function_with_parameter(self):
        expected_value_1 = "You input the parameter: Joe"
        self.assertEqual(expected_value_1, uit.a_function_with_a_parameter_but_no_user_input("Joe"))
        expected_value_2 = "You input the parameter: TMNT"
        self.assertEqual(expected_value_2, uit.a_function_with_a_parameter_but_no_user_input("TMNT"))
        expected_value_3 = "You input the parameter: Hello"
        self.assertEqual(expected_value_3, uit.a_function_with_a_parameter_but_no_user_input("Hel", "lo"))

    def test_function_with_3_user_input(self):
        with mock.patch('builtins.input', side_effect=["125", "150", "175"]):
            self.assertEqual(150, uit.a_function_with_no_paramters_that_asks_for_user_input())
    def test_function_with_3_user_input2(self):
        with mock.patch('builtins.input', side_effect=["-100", "3", "100"]):
            self.assertEqual(1, uit.a_function_with_no_paramters_that_asks_for_user_input())

    @patch('main.user_input_types.a_function_with_no_parameters_or_input', return_value=-45)
    def test_change_called_function_result(self, input):
        self.assertEqual(0, uit.a_function_that_calls_another_function())

    @patch('main.user_input_types.a_function_with_no_parameters_or_input', return_value=55)
    def test_change_called_function_result2(self, input):
        self.assertEqual(100, uit.a_function_that_calls_another_function())
if __name__ == '__main__':
    unittest.main()
