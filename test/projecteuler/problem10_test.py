import unittest
from projecteuler.problem10 import * #@UnusedWildImport

class Test(unittest.TestCase):

    def test_primes_below(self):
        self.assertEqual([2,3,5,7], primes_below(10))

    def test_solve(self):
        self.assertEqual(17, solve(10))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()