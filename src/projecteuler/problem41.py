'''
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
'''

from sieve import gen_sieve_eratosthenes
from permutation import all_perms
from number import is_pandigital
from prime import miller_rabin
import time

    
def solve():
    result = 0 #@UnusedVariable
    
    start = time.clock()
    pandigits = '123456789'
    primes = []
    for i in range(9, 0, -1):
        for pandigital_num in all_perms(pandigits[:i]):
            n = int(pandigital_num)
            if(miller_rabin(n)):
                primes.append(n)
        if len(primes) > 0:
            break

    result = max(primes)     
    print("The largest n-digit pandigital prime is %(result)s" % vars())
    print(time.clock() - start)
if __name__ == "__main__":
    solve()




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
