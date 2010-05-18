'''
What is the smallest number divisible by each of the numbers 1 to 20?
'''
from sieve import gen_sieve_eratosthenes

from projecteuler import product_of
import math

def primes_until(ceiling):
    primes = [p for p in gen_sieve_eratosthenes(ceiling)]
    if(primes[-1] > ceiling): 
        return primes[0:-1]
    else:
        return primes

def max_power_of_x_below_y(x, y):
    return int(math.log(y, x))

def solve(ceiling):
    factors = []
    for p in primes_until(ceiling):
        factor = p**max_power_of_x_below_y(p, ceiling)
        factors.append(factor)
    return product_of(factors)
       

result = solve(20)
print("The smallest number divisible by each of the numbers 1 to 20" 
      + " is %(result)d" % vars())
