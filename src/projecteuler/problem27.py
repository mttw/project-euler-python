"""
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

from sieve import sieve_eratosthenes
from projecteuler import list_to_dict
from prime import miller_rabin
from itertools import product
from itertools import takewhile
from test.test_itertools import take


def quadratics(a,b, start):
    # produces sequence: n^2 + an + b
    n = start
    while(1):
        yield n**2 + a*n + b
        n += 1


if __name__ == '__main__':
    primes = list_to_dict(sieve_eratosthenes(10**6), True)
    print("Prepared sieve")
        
    (ma, mb, mn) = (0,0,0)
    for (a, b) in product(range(-1000,1000), repeat=2):
            if not (mn**2 + a*mn + b) in primes:
                continue
            consecutive_primes = list(takewhile(lambda q: q in primes, quadratics(a,b, 0)))
            if(len(consecutive_primes) > mn):
                (ma, mb, mn) = (a, b, len(consecutive_primes))
    
    result = ma*mb
    print("The coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n are (%(ma)d, %(mb)d)" % vars())    
    print("Their product is %(result)d" % vars())