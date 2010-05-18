import unittest
from projecteuler.problem7 import * #@UnusedWildImport

class Test(unittest.TestCase):


    def test_find_ith_prime(self):
        self.assertEqual(2, find_ith_prime(1))
        self.assertEqual(3, find_ith_prime(2))
        self.assertEqual(5, find_ith_prime(3))
        self.assertEqual(7, find_ith_prime(4))
        self.assertEqual(11, find_ith_prime(5))
        self.assertEqual(13, find_ith_prime(6))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()