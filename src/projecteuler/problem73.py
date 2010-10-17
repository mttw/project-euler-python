'''
How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?
'''
from fractions import Fraction, gcd
import math
import time



def solve(p,q, D):
    ct = 0
    for d in range(4, D+1):
        start = int(p*d) + 1
        end = int(math.ceil(q*d))
        for n in range(start, end):
            if gcd(n,d) == 1:
                ct += 1
    return ct
if __name__ == "__main__":
#    D = 8
    D = 12000
    start = time.clock()
    result = solve(Fraction(1,3), Fraction(1,2), D)
    print("There are %(result)d fractions between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= %(D)d?" % vars())
    print(time.clock() - start)