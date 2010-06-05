'''
In the first one-thousand expansions of sqrt(2), how many fractions contain a numerator with more digits than denominator?
'''
from fractions import Fraction
from math import log10
import time

def invert(fraction):
    return Fraction(fraction.denominator, fraction.numerator)

def expansions_of_sqrt2(n):
    x = Fraction(1,2)
    for i in range(0,n):
        yield Fraction(1) + x
        x = invert(Fraction(2) + x)

def diff_digits(a, b):
    return int(log10(a)) - int(log10(b)) 

def solve(N):
    expansions_with_more_digits_in_numerator = \
        filter(lambda f: diff_digits(f.numerator, f.denominator) > 0,
               expansions_of_sqrt2(N))
    return len(expansions_with_more_digits_in_numerator)

if __name__ == "__main__":
    N = 1000
    result = solve(N)
    print("In the first %(N)d expansions of sqrt(2), the number fractions of containing a numerator with more digits than denominator is %(result)d" % vars())
