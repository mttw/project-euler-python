'''
By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
'''
from fractions import Fraction
import time

def solve(q, D):
    candidates = filter(lambda p: p < q, [Fraction(int(q*d),d) for d in range(1,D+1)])
    return max(candidates)

if __name__ == "__main__":
    D = 10**6
    start = time.clock()
    p = solve(Fraction(3,7), D)
    result = p.numerator
    print("The numerator of the fraction %(p)s immediately to the left of 3/7 is %(result)d" % vars())
    print(time.clock() - start)
