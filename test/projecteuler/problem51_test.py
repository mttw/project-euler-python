import unittest
from projecteuler.problem51 import * #@UnusedWildImport

class Test(unittest.TestCase):


    def test_transform_starred_2(self):
        self.assertEqual([], transform_starred(1, 2))
        self.assertEqual([], transform_starred(12, 2))
        self.assertEqual([], transform_starred(123, 2))

        self.assertEqual(['**'], transform_starred(11, 2))
        self.assertEqual(['**2'], transform_starred(112, 2))
        self.assertEqual(['*2*'], transform_starred(121, 2))
        self.assertEqual(['**1', '*1*', '1**'], transform_starred(111, 2))

        self.assertEqual(['**222', '11**2', '11*2*', '112**'], transform_starred(11222, 2))

    def test_transform_starred_3(self):
        self.assertEqual(['***'], transform_starred(111, 3))
        self.assertEqual(['***2'], transform_starred(1112, 3))
        self.assertEqual(['11***'], transform_starred(11222, 3))
        self.assertEqual(['***12', '**1*2', '*1**2', '1***2'], transform_starred(11112, 3))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()