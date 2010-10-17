'''
Find the value of n, 1 <= n <= 10^7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.
'''
from fractions import gcd
from itertools import takewhile, count, combinations
import time
from sieve import factorize_with_eratosthenes, sieve_eratosthenes,\
    gen_sieve_eratosthenes, print_sieve_stats
from projecteuler import product_of
import math
from permutation import produce
import permutation
from number import lsqrt


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
        
def powers_below(x, N, start=1):
    def powers(x, start):
        y = x**start
        while True:
            yield y
            y *= x
            
    return list(takewhile(lambda y: y <= N, powers(x, start)))  

#def solve1(N):
#    primes = sieve_eratosthenes(N)
#    print("Sieve prepared")
#
#    min_frac = N
#    min_number = N
#    primes.reverse()
#    print(len(primes))
##    combos = sorted(combinations(primes[-1000:], 2), cmp=lambda (p1,q1),(p2,q2): cmp(p1*q1, p2*q2))
#    print("Primes reversed")
#    for p in primes:
#        for p_power in powers_below(p, N):
#            # only distinct primes are considered
#            phi = p_power - p_power/p
#            if permutation.is_permuted(p_power, phi):
#                frac = float(p_power)/phi
#                if frac < min_frac:
#                    print(p_power, phi, frac)
#                    min_frac = frac
#                    min_number = p_power
#    return min_number

#def solve(N):
#    primes = sieve_eratosthenes(lsqrt(N)*2)
#    print("Sieve prepared")
#
#    min_frac = N
#    min_number = N
#    print(len(primes))
#    combos = combinations(primes, 2)
#    combos = filter(lambda primes: product_of(primes) <= N, combos)
##    combos = sorted(combinations(primes, 2), cmp=lambda (p1,q1),(p2,q2): cmp(p1*q1, p2*q2))
#    print("Prime tuples sorted / filtered")
#    for primes in combos:
#        # only distinct primes are considered
#        if len(primes) != len(set(primes)):
#            continue 
#        n = product_of(primes)
#
#        if n > N:
#            continue
#
#        phi = product_of([(p-1) for p in primes])
#        if permutation.is_permuted(n, phi):
#            frac = float(n)/phi
#            if frac < min_frac:
#                print(n, phi, frac)
#                min_frac = frac
#                min_number = n
#    return min_number


def solve(N):
    primes = sieve_eratosthenes(lsqrt(N)*2)
    print_sieve_stats(primes)
    min_frac = N
    min_number = N
    for step in range(1, 500):
        for (p, q) in [(primes[i], primes[i-step]) for i in range(len(primes)-1, step-1, -1)]:
            for (p_power, q_power) in zip(powers_below(p, N), powers_below(q, N)):
                n = p_power*q_power
                if n > N:
                    continue
        
                phi = (p_power - p_power/p)*(q_power - q_power/q)
                if permutation.is_permuted(n, phi):
                    frac = float(n)/phi
                    if frac < min_frac:
                        print(n, p, q, phi, frac, step)
                        min_frac = frac
                        min_number = n
    return min_number

    
if __name__ == "__main__":
    
    N = 10**7
    start = time.clock()
    result = solve(N)
    
    
    print("The value of n, 1 <= n <= %(N)d, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum is %(result)d" % vars())
    print("duration", time.clock()-start)
    