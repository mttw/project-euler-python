import unittest
from permutation import * #@UnusedWildImport

class Test(unittest.TestCase):

    def test_produce(self):
        self.assertEqual([[1]], [e for e in produce([[1]])])
        self.assertEqual([[1],[2]], [e for e in produce([[1,2]])])

        self.assertEqual([[1, 'a'], [2, 'a'], [1, 'b'], [2, 'b']], [e for e in produce([[1,2], ['a', 'b']])])

        self.assertEqual([['1', 'a', 'X'], ['2', 'a', 'X'], ['1', 'b', 'X'], ['2', 'b', 'X'], ['1', 'a', 'Y'], ['2', 'a', 'Y'], ['1', 'b', 'Y'], ['2', 'b', 'Y']], 
                         [e for e in produce(['12', 'ab', 'XY'])])

        self.assertEqual(8, len([e for e in produce(['12', 'ab', 'XY'])]))
        self.assertEqual(12, len([e for e in produce(['123', 'ab', 'XY'])]))


        #self.assertEqual([[1], [2]], [[1,2]])



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()