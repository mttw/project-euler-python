'''
How many elements would be contained in the set of reduced proper fractions for d <= 1,000,000?
'''

import time

from sieve import sieve_eratosthenes
from prime import factorizations_below


def phi_of_factorization(factorization):
    phi = 1
    for (p,exp) in factorization:
        phi *= p**(exp - 1)*(p-1)
    return phi

def solve(D):
    primes = sieve_eratosthenes(D)
    factorizations = list(factorizations_below(D, primes))
    assert len(factorizations)+1 == D 
    return sum([phi_of_factorization(factorization) for factorization in factorizations])


if __name__ == "__main__":
    D = 10**3
    start = time.clock()
    result = solve(D)

    print("There are %(result)d elements in the set of reduced proper fractions for d <= %(D)d?" % vars())
    print(time.clock() - start)