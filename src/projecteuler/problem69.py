'''
Find the value of n  1,000,000 for which n/phi(n) is a maximum.
'''
from fractions import gcd
from itertools import takewhile, count
import time


from sieve import factorize_with_eratosthenes, sieve_eratosthenes,\
    gen_sieve_eratosthenes
from projecteuler import product_of
import math
from permutation import produce

def euler_phi(n):
    if n == 1:
        return 1
    return len(filter(lambda i: gcd(i,n) == 1, range(1,n)))

def find_product_primes_below(N):
    prod = 1
    l = []
    for p in gen_sieve_eratosthenes():
        prod *= p
        if prod >= N:
            return l
        l.append(p)
        
def powers_below(x, N, start=0):
    def powers(x, start):
        y = x**start
        while True:
            yield y
            y *= x
            
    return list(takewhile(lambda y: y <= N, powers(x, start)))  


def solve(N):
    primes = find_product_primes_below(N)
    factors_set = [[n for n in powers_below(p, N, 1)] for p in primes]

    max_frac = 0.0
    max_number = 0
    for factors in produce(factors_set):
        n = product_of(factors)
        if n > N:
            continue
        phi = product_of([num - num/p for (num,p) in zip(factors, primes)])

        frac = float(n)/phi
        if frac > max_frac:
            print(n, frac, factors)
            max_frac = frac
            max_number = n
    return max_number

    
if __name__ == "__main__":
        
    start = time.clock()
    N = 1000000
    result = solve(N)
    
    
    print("The value of n <= %(N)d for which n/phi(n) is a maximum is %(result)d" % vars())
    print(time.clock()-start)
    