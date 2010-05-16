import unittest
from fibonacci import *
class Test(unittest.TestCase):


    def test_fibonacci(self):
        self.assertEqual(0, fibonacci(0))
        self.assertEqual(1, fibonacci(1))
        self.assertEqual(1, fibonacci(2))
        self.assertEqual(2, fibonacci(3))
        self.assertEqual(3, fibonacci(4))
        self.assertEqual(5, fibonacci(5))

    def test_fibonaccis(self):
        f = fibonaccis()
        self.assertEqual(0, f.next())
        self.assertEqual(1, f.next())
        self.assertEqual(1, f.next())
        self.assertEqual(2, f.next())
        self.assertEqual(3, f.next())
        self.assertEqual(5, f.next())
        self.assertEqual(8, f.next())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_name']
    unittest.main()