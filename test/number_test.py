import unittest
from number import * #@UnusedWildImport

class Test(unittest.TestCase):


    def test_is_square(self):
        self.assertTrue(is_square(4))
        self.assertFalse(is_square(5))

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(1))
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(101))
        
        self.assertFalse(is_palindrome(12))
        self.assertFalse(is_palindrome(123))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()