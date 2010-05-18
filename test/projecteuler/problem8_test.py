import unittest
from projecteuler.problem8 import * #@UnusedWildImport

class Test(unittest.TestCase):


    def test_consecutive_subsets_of(self):
        self.assertEqual(['1', '2', '3'], consecutive_subsets_of('123', 1))
        self.assertEqual(['12', '23'], consecutive_subsets_of('123', 2))
        self.assertEqual(['123'], consecutive_subsets_of('123', 3))

    def test_solve(self):
        self.assertEqual(4, solve(1234,1))
        self.assertEqual(4, solve(4321,1))

        self.assertEqual(12, solve(1234,2))

        self.assertEqual(81, solve(1119911111111,2))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()