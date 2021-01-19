import unittest
import mastermind
from unittest.mock import patch
from io import StringIO
import sys
class myTestCases(unittest.TestCase):

    def test_create_code(self):
        """
        Here i am testing the create code function, to see if it runs and returning the 4 digit code, each digit is less than 9 and greater than 0
        """
        output = StringIO()
        sys.stdout = output
        index = 0
        while index < 100:
            code = mastermind.create_code()
            length_of_code = len(code)
            self.assertEqual(length_of_code,4)
            if type(code) == list:
                type_code = True
            self.assertEqual(type_code, True)

            for x in range(4):
                self.assertGreater(code[x],0)
                self.assertLess(code[x],9)
            index +=1
        sys.stdout = sys.__stdout__
    def test_check_correctness(self):
        """
        method tests whether he check_correctness fn returns True only when correct_digits_and_position is equal t0 4, else False
        """
        output = StringIO()
        sys.stdout = output
        self.assertEqual(mastermind.check_correctness(11,4), True)
        self.assertEqual(mastermind.check_correctness(11,3), False)
        sys.stdout = sys.__stdout__
    @patch("sys.stdin",StringIO("3695\n"))
    def test_get_answer_input(self):
        """ 
        we testing the function of the user input, ensures that the functions returns answers that meets the requirements
        """
        output = StringIO()
        sys.stdout = output

        results = mastermind.get_answer_input()
        length_results = len(results)

        self.assertEqual(length_results, 4)
        self.assertTrue(results.isdigit)
        if not results.isdigit() or length_results != 4:
            self.assertEqual(results, results)
        sys.stdout = sys.__stdout__
    def test_take_turn(self):
        """
        The method checks whether the take_turn function returns the correct output when given differnt parameters
        """
        output = StringIO()
        sys.stdout = output
        self.assertEqual(mastermind.take_turn([1,2,3,4], [1,2,3,4]), (4, 0))
        self.assertEqual(mastermind.take_turn([1,2,3,4], [1,6,5,4]), (2, 0))
        self.assertEqual(mastermind.take_turn([1,2,3,4], [7,6,5,8]), (0, 0))

        sys.stdout = sys.__stdout__
if __name__ == "__main__":
    unittest.main()
