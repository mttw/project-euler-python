import unittest
from projecteuler.problem4 import solve

class Test(unittest.TestCase):


    def test_solve(self):
        self.assertEqual(9009, solve(range(10, 100)))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()