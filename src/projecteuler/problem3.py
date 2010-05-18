'''
What is the largest prime factor of the number 600851475143 ?
'''
from sieve import factorize_with_eratosthenes
import time
        
def solve(number):
    factors = factorize_with_eratosthenes(number)
    sorted_primes = sorted(factors)
    print("Factors of %(number)d: %(sorted_primes)s" % vars())
    return sorted_primes[-1]



number = 600851475143
start = time.clock()

result = solve(number)

print("The largest prime factor of %(number)d is %(result)d" % vars())
duration = time.clock() - start
print("Duration: %(duration).3fs" % vars())