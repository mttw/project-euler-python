import unittest
from projecteuler.problem5 import * #@UnusedWildImport

class Test(unittest.TestCase):


    def test_max_power_of_x_below_y(self):
        self.assertEqual(0, max_power_of_x_below_y(2, 1))
        self.assertEqual(1, max_power_of_x_below_y(2, 2))
        self.assertEqual(1, max_power_of_x_below_y(2, 3))
        self.assertEqual(2, max_power_of_x_below_y(2, 4))
        self.assertEqual(4, max_power_of_x_below_y(2, 16))
        self.assertEqual(4, max_power_of_x_below_y(2, 31))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()