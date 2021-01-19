import unittest
import super_algos

class   MyTestCases(unittest.TestCase):

    def test_find_min(self):
        """the test function checks if a list is empty or a non intiger is in the list, it returns -1. Also tests that the minimum int in the list in rerurned"""

        self.assertEqual(super_algos.find_min(['']), -1) 
        self.assertEqual(super_algos.find_min([1,'b','d']),-1)
        self.assertEqual(super_algos.find_min([7,6,8,9,3,11]),3)

    def test_sum_all(self):
        """the test function checks if a list is empty or a non intiger is in the list, it returns -1. Also tests that a function returns the sum of the intigers in a list"""
        self.assertEqual(super_algos.sum_all(['']), -1) 
        self.assertEqual(super_algos.sum_all([1,'b','d']),-1)
        self.assertEqual(super_algos.sum_all([3,6,8,9,3,11]),40)

    def test_fint_possible_strings(self):

        self.assertEqual(super_algos.find_possible_strings(['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'], 2), ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'], 2)

if __name__ == '__main__':                          
    unittest.main()