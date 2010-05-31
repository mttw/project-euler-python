'''
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
'''

from permutation import produce
from number import is_prime
import time

import sys
import random

def toBinary(n):
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
    b = toBinary(n - 1)
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
    for j in xrange(1, s + 1): #@UnusedVariable
        a = random.randint(1, n - 1)
        if (test(a, n)):
            return False # n is complex
    return True # n is prime


def generate_left_truncated_string(s):
    return [s[i:] for i in range(len(s))]
        
def generate_right_truncated_string(s):
    return [s[:i] for i in range(len(s), 0, -1)]


def solve():
    result = 0 #@UnusedVariable
    start = time.clock()
    i = 0
    primes = {}
    truncatable_primes = []
    for i in range(0, 7):
        border = ['37']
        if i == 0:
            border = ['2357']
        digit_sets = border + i*['1379'] + border
        for digits in produce(digit_sets):
            number = "".join(digits)
            nums = sorted(set([int(n) for n in generate_left_truncated_string(number)] + [int(n) for n in generate_right_truncated_string(number)]))
            all_are_primes = True
            for n in nums:
                if n < 10:
                    continue
                try:
                    is_p = primes[n]
                except KeyError, e:
                    is_p = miller_rabin(n, 20)
                    primes[n] = is_p 

                if not is_p:
                    all_are_primes = False
            if all_are_primes:
                truncatable_primes.append(int(number)) 
                
        
    result = sum(truncatable_primes)
    print("The sum of the only eleven primes that are both truncatable from left to right and right to left is %(result)d" % vars())
    print(truncatable_primes)
    print(time.clock() - start)
if __name__ == "__main__":
    solve()


