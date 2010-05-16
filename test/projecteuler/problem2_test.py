import unittest
from projecteuler.problem2 import solve

class Test(unittest.TestCase):


    def test_solve(self):
        self.assertEqual(0, solve(1))
        self.assertEqual(2, solve(3))
        self.assertEqual(10, solve(10))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()