'''
what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%
'''
from itertools import count
from sieve import sieve_eratosthenes
from fractions import Fraction
from prime import miller_rabin
import time
from projecteuler import list_to_dict

def spiral_layer_edges():
    layer = [1]
    yield layer
    for k in count(1):
        latest = layer[-1]
        layer = [latest + 2*i*k for i in range(1, 5)]
        yield layer

def solve(ratio):
#    ps = sieve_eratosthenes(10**8)
#    highest_prime = ps[-1]
#    primes = list_to_dict(ps, True)

#    print('Sieve prepared')
    num_numbers = 0
    num_primes = 0
    i = 0
    for layer in spiral_layer_edges():
        i += 1
        for n in layer:
            if miller_rabin(n, 50):
                num_primes += 1
        num_numbers += len(layer)
        if Fraction(num_primes, num_numbers) < ratio and i > 1:
            print(num_primes, num_numbers)
            return 1 + 2*(i-1)

if __name__ == "__main__":
    ratio = 0.1
    start = time.clock()
    result = solve(ratio)
    print(time.clock() - start)
    print("The side length of the square spiral for which the ratio of primes along both diagonals first falls below %(ratio).2f is %(result)d" % vars())
