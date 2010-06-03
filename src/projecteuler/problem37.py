'''
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
'''

from permutation import produce
from prime import miller_rabin
import time


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


