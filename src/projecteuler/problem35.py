'''
How many circular primes are there below one million?
'''

from sieve import gen_sieve_eratosthenes, is_prime
from number import circulate
from projecteuler import boolean_product_of
import time



def is_circular_prime(p, sieve):
    # assuming p is prime
    for n in circulate(p)[1:]:
        if not is_prime(n, sieve):
            return False
            
    return True

def solve(N):
    result = 0 #@UnusedVariable
    
    start = time.clock()
    sieve = {}
    for p in gen_sieve_eratosthenes(N + 1):
        sieve[p] = True
        
    print('Sieve prepared')
    circular_primes = []
    for p in sorted(sieve.keys()):
        if is_circular_prime(p, sieve):
            circular_primes.append(p)
    
    print(circular_primes)
    result = len(circular_primes) #@UnusedVariable
    print("The number of circular primes below %(N)d is %(result)d" % vars())
    print(time.clock() - start)
if __name__ == "__main__":
    solve(10**6)




#def find_first(l, matching_func):
#    for e in l:
#        if(matching_func(e)):
#            return e
#    return None
    

#def is_prime(n, sieve_map):
#    try:
#        sieve_map[n]
#        return True
#    except KeyError, e:
#        return False
