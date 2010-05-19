import unittest
from grid import * #@UnusedWildImport

class Test(unittest.TestCase):

    def test_consecutive_subsets_of(self):
        self.assertEqual(['1', '2', '3'], consecutive_subsets_of('123', 1))
        self.assertEqual(['12', '23'], consecutive_subsets_of('123', 2))
        self.assertEqual(['123'], consecutive_subsets_of('123', 3))
        
        self.assertEqual([], consecutive_subsets_of('12', 3))

    def test_is_matrix(self):
        self.assertTrue(is_matrix([[1,2],[3,4]]))
        self.assertFalse(is_matrix([[1],[2,3]]))


    def test_transposed(self):
        self.assertEqual([[1,3],[2,4]], transposed([[1,2],[3,4]]))
        self.assertEqual([[1,4],[2,5],[3,6]], transposed([[1,2,3],[4,5,6]]))

    def test_diag(self):
        self.assertEqual([[1],[3,2], [4]], diag([[1,2],[3,4]]))
        self.assertEqual([[1],[4,2],[7,5,3],[8,6],[9]], diag([[1,2,3],[4,5,6],[7,8,9]]))

    def test_diag2(self):
        self.assertEqual([[2],[4,1], [3]], diag2([[1,2],[3,4]]))
        self.assertEqual([[3],[6,2],[9,5,1],[8,4],[7]], diag2([[1,2,3],[4,5,6],[7,8,9]]))



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()