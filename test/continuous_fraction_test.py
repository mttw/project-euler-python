import unittest
from continuous_fraction import * #@UnusedWildImport

class Test(unittest.TestCase):

    def test_continuous_fraction_from_sqrt(self):
        self.assertEqual(ContinuousFraction([1], [2]), ContinuousFraction.from_sqrt(2))
        self.assertEqual(ContinuousFraction([1], [1,2]), ContinuousFraction.from_sqrt(3))
        self.assertEqual(ContinuousFraction([2], [4]), ContinuousFraction.from_sqrt(5))
        self.assertEqual(ContinuousFraction([2], [1,1,1,4]), ContinuousFraction.from_sqrt(7))
        self.assertEqual(ContinuousFraction([3], [1,1,1,1,6]), ContinuousFraction.from_sqrt(13))
        
    def test_continuous_fraction_to_fraction(self):
        sqrt2 = ContinuousFraction([1],[2])
        self.assertEqual(Fraction(1), sqrt2.to_fraction(1))
        self.assertEqual(Fraction(3,2), sqrt2.to_fraction(2))
        self.assertEqual(Fraction(7,5), sqrt2.to_fraction(3))
        self.assertEqual(Fraction(17,12), sqrt2.to_fraction(4))
        self.assertEqual(Fraction(41,29), sqrt2.to_fraction(5))

        sqrt23 = ContinuousFraction([4],[1,3,1,8])
        self.assertEqual(Fraction(4), sqrt23.to_fraction(1))
        self.assertEqual(Fraction(5), sqrt23.to_fraction(2))
        self.assertEqual(Fraction(19,4), sqrt23.to_fraction(3))

    def test_irrational(self):
        self.assertEqual(Irrational(1,1,2), Irrational(1,1,2))
        self.assertEqual(Irrational(3,0,2), Irrational(1,1,4))
        self.assertEqual(Irrational(5,0,2), Irrational(1,1,16))
        self.assertEqual(Irrational(7,0,6), Irrational(1,1,36))


    def test_irrational_conjugate(self):
        z = Irrational(4,1,23)
        self.assertEqual(Irrational(4,-1,23), z.conjugate())
        self.assertEqual(Irrational(Fraction(-4,7),Fraction(1,7),23), z.invert())
        self.assertEqual(z.invert(), Irrational(1,0,23)/z)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()