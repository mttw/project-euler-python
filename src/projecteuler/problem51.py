'''
By replacing the 1st digit of *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''
from itertools import combinations
from sieve import sieve_eratosthenes
import math

def find_all_digit_indices(n, digit):
    digits = str(n)
    return filter(lambda i: int(digits[i]) == digit, 
                  range(len(digits)))
            

def indices_of_same_digist(n, k=2):
    groups = []
    distinct_digits = set([int(d) for d in str(n)])
    for digit in distinct_digits:
        indices = find_all_digit_indices(n, digit)
        if len(indices) >= k:
            groups.append(indices)
    return groups

def mask_string(s, indices, replacment = '*'):
    masked_string = ''
    for i in range(len(s)):
        if i in indices: 
            masked_string += '*'
        else: 
            masked_string += s[i]
    return masked_string
    
def transform_starred(n, k):
    starred_numbers = []

    for group in indices_of_same_digist(n, k):
        if len(group) >= k:
            for combination in combinations(group, k):
                starred_numbers.append(mask_string(str(n), combination, '*'))
    
    return starred_numbers


def solve(N, ceiling):
    primes = sieve_eratosthenes(ceiling)
    print('Sieve prepared')
    mp = {}
    K = int(math.log10(ceiling))

    for k in range(2, K):
        print('k=' + str(k))
        for p in primes:
            for starred_number in transform_starred(p, k):
                try:
                    mp[starred_number].append(p)
                except KeyError, e:
                    mp[starred_number] = [p]
        
    max_primes = 0
    result_primes = None
    for (sn, primes) in mp.items():
        if len(primes) > max_primes:
            max_primes = len(primes)
            result_primes = primes
    
    assert N == max_primes
    print(result_primes)
    result = sorted(result_primes)[0]
    print("The smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family is %(result)d" % vars())

if __name__ == "__main__":
    ceiling = 10**6
    solve(8, ceiling)
