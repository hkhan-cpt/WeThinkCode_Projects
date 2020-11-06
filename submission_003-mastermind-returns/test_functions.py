import unittest
import mastermind
import sys
import io
from io import StringIO
from mastermind import check_correctness
from unittest.mock import patch
from mastermind import get_answer_input
from mastermind import take_turn


class TestFunctions(unittest.TestCase):
    def test_create_code(self):
        """Checks that the function returns a list with 4 numbers, ensuring neither 0 nor 9 is present.
        Calls create_code a hundred times."""

        for counter in range(100):
            result = mastermind.create_code()

            self.assertNotIn(0, result)
            self.assertNotIn(9, result)
            self.assertEqual(4, len(result))


    def test_check_correctness(self):
        """Checks for different combinations of parameters which results in a true 
        or false return value from the function."""

        mastermind.check_correctness 

        sys.stdout = io.StringIO()
        self.assertTrue(check_correctness(4, 4))
        self.assertEqual(sys.stdout.getvalue(), "Congratulations! You are a codebreaker!\n")

        sys.stdout = io.StringIO()
        self.assertFalse(check_correctness(3, 6))
        self.assertEqual(sys.stdout.getvalue(), "Turns left: 6\n")


    @patch("sys.stdin", StringIO("123\n12345\n1234\n"))
    def test_get_answer_input(self):
        """Checks that the function returns a string with 4 numbers and repeatedly asks
        the user for input until the condition is satisfied. Used mocking to mimic the input 
        needed from the user."""

        mastermind.get_answer_input
        
        sys.stdout = io.StringIO()
        self.assertEqual(get_answer_input(), "1234")
        self.assertEqual(sys.stdout.getvalue(), """Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: """)


    @patch("sys.stdin", StringIO("5678\n4523\n1278\n1243\n1234\n"))
    def test_take_turn(self):
        """Checks whether the returned parameters are updated correctly based on different combinations.
        Used mocking to mimic the input needed from the user."""

        mastermind.take_turn

        self.assertEqual(take_turn([1, 2, 3, 4]), (0, 0))
        self.assertEqual(take_turn([1, 2, 3, 4]), (0, 3))
        self.assertEqual(take_turn([1, 2, 3, 4]), (2, 0))
        self.assertEqual(take_turn([1, 2, 3, 4]), (2, 2))
        self.assertEqual(take_turn([1, 2, 3, 4]), (4, 0))


if __name__ == "__main__":
    unittest.main()
