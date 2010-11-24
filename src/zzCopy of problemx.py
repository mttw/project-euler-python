'''

'''

from sieve import sieve_eratosthenes
from itertools import product
from time import time
start = time()

def compare(n1,n2):
    n1s = list(str(n1))
    n2s = list(str(n2))
    n1s.sort()
    n2s.sort()
    if n1s == n2s: return True
    return False

# Big primes will be the closest to 1 for p/phi(p), since the 
# difference between p and phi(p) is pretty much negligible, but 
# primes will never be permutations of their phi(p) values.
# product of two primes should still be relatively close to 1 for n/phi(n)
# compared to normal numbers.
# phi(p) = p-1 and phi(pq) = phi(p) * phi(q) so products of primes is good for
# the math too.
# Obviously we need to keep our products of primes below the limit,
# and the bigger the primes, the smaller the n/phi(n).

limit = 10**7
minimum = 1000000
ans = 0
primes = sieve_eratosthenes(int((limit**0.5)*2))
for pp in product(primes[100:], repeat=2):
    n = pp[0]*pp[1]
    if n > limit: continue
    phi_n = (pp[0]-1)*(pp[1]-1)
    if compare(n,phi_n):
        div = float(n)/phi_n
        if div < minimum:
            minimum = div
            ans = n

print ans
print time()-start

