import unittest
from projecteuler.problem1 import is_multiple_of_3_or_5

class Test(unittest.TestCase):


    def test_is_multiple_of_3_or_5(self):
        self.assertTrue(is_multiple_of_3_or_5(3))
        self.assertTrue(is_multiple_of_3_or_5(5))

        self.assertTrue(is_multiple_of_3_or_5(6))
        self.assertTrue(is_multiple_of_3_or_5(15))
        
        self.assertFalse(is_multiple_of_3_or_5(2))
        self.assertFalse(is_multiple_of_3_or_5(4))
        self.assertFalse(is_multiple_of_3_or_5(7))
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()