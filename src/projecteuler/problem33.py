'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that ^(49)/_(98) = ^(4)/_(8), which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

'''

from fractions import Fraction
from number import product_of

def produce_simplifications(numerator, denominator, exclude=0):
    s = []
    num_digits = str(numerator)
    denom_digits = str(denominator)
    for i in range(len(num_digits)):
        for j in range(len(denom_digits)):
            if num_digits[i] == denom_digits[j] and num_digits[i] != str(exclude):
                n = int(num_digits[0:i] + num_digits[i+1:])
                d = int(denom_digits[0:j] + denom_digits[j+1:])
                s.append((n,d))
    return s


def is_curious_fraction(numerator, denominator):
    f = Fraction(numerator, denominator)
    for (n, d) in produce_simplifications(numerator, denominator):
        if d > 0:
            simplified_fraction = Fraction(n, d)
            if f == simplified_fraction:
                return True
    return False

def solve():
    curious_fractions = []
    for n in range(10, 100):
        for d in range(n+1, 100):
            if is_curious_fraction(n, d):
                curious_fractions.append((n, d))
    product = reduce(lambda x, y: x*y, ([Fraction(n, d) for (n, d) in curious_fractions])) #@UnusedVariable
    result = product.denominator
    print("The fractions are %(curious_fractions)s" % vars())
    print("The value of the denominator is %(result)d" % vars())

if __name__ == "__main__":
    solve()
