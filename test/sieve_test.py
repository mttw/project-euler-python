import unittest
from sieve import * #@UnusedWildImport

class Test(unittest.TestCase):


    def test_gen_sieve_eratosthenese(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41], 
                         [p for p in gen_sieve_eratosthenes(40)])

        # TODO fix this test failure
        self.assertEqual([2, 3, 5, 7], 
                         [p for p in gen_sieve_eratosthenes(10)])

    def test_factorize_with_eratosthenes(self):
        self.assertEqual([1], factorize_with_eratosthenes(1))
        self.assertEqual([2], factorize_with_eratosthenes(2))
        self.assertEqual([2, 2], factorize_with_eratosthenes(4))
        self.assertEqual([2, 3], factorize_with_eratosthenes(6))
        self.assertEqual([3, 17], factorize_with_eratosthenes(51))
        self.assertEqual([53], factorize_with_eratosthenes(53))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()