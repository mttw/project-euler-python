'''
Find the 10001st prime.
'''
from sieve import gen_sieve_eratosthenes

def find_ith_prime(i):
    primes = zip(range(0, i), gen_sieve_eratosthenes())
    return primes[-1][1]    
       

result = find_ith_prime(10001)
print("The 10001st prime" 
      + " is %(result)d" % vars())
