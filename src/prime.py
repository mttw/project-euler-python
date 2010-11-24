import random
from itertools import takewhile, count
from permutation import product
from projecteuler import product_of
from number import powers_below



def product_of_factorization(pps):
    return product_of([x**exp for (x,exp) in pps])
        
def prime_powers_below(primes_base, N):
    # TODO code has to be fixed, is just an estimate for ceiling N
    prod = product_of(primes_base)
    prime_powers_base = [powers_below(p, (N*p)/prod) for p in primes_base]
    for factorization in product(prime_powers_base):
        if product_of_factorization(factorization) <= N:
            yield factorization

def factorizations_below(N, primes, **kwds):
    for r in count(1):
        prime_combinations = combine_primes_below(r, N, primes)
        if prime_combinations == []:
            break
        for ps in prime_combinations:
            for factorization in prime_powers_below(ps, N):
                yield factorization


def combine_primes_below(r, N, primes):
    pos = range(r)
    L = len(primes) 
    solutions = []
    if r > L:
        return solutions
    
    while True:    
        ps = [primes[j] for j in pos]
        prod = product_of(ps)
        if prod <= N:
            solutions.append(ps)
        
        index = -1
        for i in range(0, r):
            if pos[r-1-i] == L-1-i:
                prod = product_of(ps[:r-1-i])
                continue
            elif prod > N:
                prod = product_of(ps[:r-1-i])
                continue
            else:
                index = r-1-i
                break
        if index == -1:
            break
        pos[index] += 1
        for i in range(index+1, r):
            pos[i] = pos[i-1] + 1
    
    return solutions




def to_binary(n):
    r = []
    while (n > 0):
        r.append(n % 2)
        n = n / 2
    return r

def test(a, n):
    """
      test(a, n) -> bool Tests whether n is complex.

      Returns:
        - True, if n is complex.
        - False, if n is probably prime.
    """
    b = to_binary(n - 1)
    d = 1
    for i in xrange(len(b) - 1, -1, -1):
        x = d
        d = (d * d) % n
        if d == 1 and x != 1 and x != n - 1:
            return True # Complex
        if b[i] == 1:
            d = (d * a) % n
    if d != 1:
        return True # Complex
    return False # Prime

def miller_rabin(n, s=50):
    """
    MillerRabin(n, s = 1000) -> bool Checks whether n is prime or not

    Returns:
      - True, if n is probably prime.
      - False, if n is complex.
    """
    if n == 1:
        return False
    for j in xrange(1, s + 1): #@UnusedVariable
        a = random.randint(1, n - 1)
        if (test(a, n)):
            return False # n is complex
    return True # n is prime
