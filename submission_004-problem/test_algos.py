import unittest
import super_algos
from super_algos import find_min
from super_algos import sum_all
from super_algos import find_possible_strings


class MyTestCase(unittest.TestCase):
    def test_find_min(self):
        '''
        Checks for:
        > invalid elements in the list
        > empty list
        > list containing only one element
        > negtaive numbers
        > all positive numbers
        '''

        super_algos.find_min

        self.assertEqual(-1, find_min([2, 5, 1, "a"]))
        self.assertEqual(-1, find_min([]))
        self.assertEqual(5, find_min([5]))
        self.assertEqual(-5, find_min([2, -5, 1, 8]))
        self.assertEqual(1, find_min([2, 5, 1, 8]))
        


    def test_sum_all(self):
        '''
        Checks for:
        > invalid elements in the list
        > empty list
        > list containing only one element
        > negtaive numbers
        > all positive numbers
        '''

        super_algos.sum_all

        self.assertEqual(-1, sum_all([2, 5, 1, "a"]))
        self.assertEqual(-1, sum_all([]))
        self.assertEqual(5, sum_all([5]))
        self.assertEqual(-5, find_min([2, -5, 1, 8]))        
        self.assertEqual(16, sum_all([2, 5, 1, 8]))


    def test_find_possible_strings(self):
        '''
        Checks for:
        > invalid elements in the list
        > empty list
        > valid list for no combinations
        > valid list for 3 combinations
        '''

        super_algos.find_possible_strings

        self.assertEqual([], find_possible_strings([2, 5, 1, 8], 3))
        self.assertEqual([], find_possible_strings([], 2))
        self.assertEqual(['a','b'], find_possible_strings(["a", "b"], 1))
        self.assertEqual(['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'], find_possible_strings(["a", "b"], 3))


if __name__ == "__main__":
    unittest.main()