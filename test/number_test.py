import unittest
from number import * #@UnusedWildImport

class Test(unittest.TestCase):

    def test_is_hexagonal_number(self):
        #     1, 6, 15, 28, 45, ...
        self.assertTrue(is_hexagonal_number(1))
        self.assertTrue(is_hexagonal_number(6))
        self.assertTrue(is_hexagonal_number(15))
        self.assertTrue(is_hexagonal_number(28))
        self.assertTrue(is_hexagonal_number(45))

        self.assertFalse(is_hexagonal_number(2))
        self.assertFalse(is_hexagonal_number(3))
        self.assertFalse(is_hexagonal_number(4))
        self.assertFalse(is_hexagonal_number(5))
        self.assertFalse(is_hexagonal_number(11))

        self.assertTrue(is_hexagonal_number(hexagonal_number(1000)))
        self.assertFalse(is_hexagonal_number(hexagonal_number(1000)+1))

    def test_is_pentagonal_number(self):
        #1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
        self.assertTrue(is_pentagonal_number(1))
        self.assertTrue(is_pentagonal_number(5))
        self.assertTrue(is_pentagonal_number(12))
        self.assertTrue(is_pentagonal_number(22))
        self.assertTrue(is_pentagonal_number(35))
        self.assertTrue(is_pentagonal_number(51))
        self.assertTrue(is_pentagonal_number(70))
        
        self.assertFalse(is_pentagonal_number(2))
        self.assertFalse(is_pentagonal_number(3))
        self.assertFalse(is_pentagonal_number(4))
        self.assertFalse(is_pentagonal_number(6))

        self.assertFalse(is_pentagonal_number(10))
        self.assertFalse(is_pentagonal_number(11))
        
        self.assertTrue(is_pentagonal_number(pentagonal_number(1000)))
        self.assertFalse(is_pentagonal_number(pentagonal_number(1000)+1))

    def test_is_triangle_number(self):
        self.assertTrue(is_triangle_number(1))
        self.assertTrue(is_triangle_number(3))
        self.assertTrue(is_triangle_number(6))
        self.assertTrue(is_triangle_number(10))
        self.assertTrue(is_triangle_number(15))
        
        self.assertFalse(is_triangle_number(2))
        self.assertFalse(is_triangle_number(4))
        self.assertFalse(is_triangle_number(5))
        self.assertFalse(is_triangle_number(11))

        self.assertTrue(is_triangle_number(triangle_number(1000)))
        self.assertFalse(is_triangle_number(triangle_number(1000)+1))



    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(6))

    def test_is_pandigital(self):
        self.assertTrue(is_pandigital(1))

        self.assertTrue(is_pandigital(12))
        self.assertTrue(is_pandigital(21))
        
        self.assertTrue(is_pandigital(123))
        self.assertTrue(is_pandigital(312))

        self.assertFalse(is_pandigital(0))
        self.assertFalse(is_pandigital(2))

        self.assertFalse(is_pandigital(13))
        self.assertFalse(is_pandigital(11))
        self.assertFalse(is_pandigital(23))
        self.assertFalse(is_pandigital(31))


    def test_divisors_of(self):
        self.assertEquals([1], sorted(divisors_of(1)))
        self.assertEquals([1,2], sorted(divisors_of(2)))
        self.assertEquals([1,3], sorted(divisors_of(3)))
        self.assertEquals([1,2,4], sorted(divisors_of(4)))
        self.assertEquals([1,5], sorted(divisors_of(5)))
        self.assertEquals([1,2,3,6], sorted(divisors_of(6)))

    def test_square_divisors_of(self):
        self.assertEquals([], square_divisors_of(1))
        self.assertEquals([], square_divisors_of(2))
        self.assertEquals([], square_divisors_of(3))
        self.assertEquals([4], square_divisors_of(4))
        self.assertEquals([4], square_divisors_of(8))
        self.assertEquals([4], square_divisors_of(20))
        self.assertEquals([4,16], square_divisors_of(16))

        self.assertEquals([], square_divisors_of(35))
        self.assertEquals([4,9,36], square_divisors_of(36))


    def test_is_square(self):
        self.assertTrue(is_square(4))
        self.assertFalse(is_square(5))

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(1))
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(101))
        
        self.assertFalse(is_palindrome(12))
        self.assertFalse(is_palindrome(123))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()