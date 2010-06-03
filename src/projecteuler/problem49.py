'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from sieve import gen_sieve_eratosthenes
from itertools import combinations 

# assumption: sequence is ordered
# should have at least 3 elements
def has_arithmetic_property(sequence):
    if len(sequence) <= 2:
        return False
    diff = sequence[1] - sequence[0]
    for i in range(2, len(sequence)):
        if (sequence[i] - sequence[i-1]) != diff:
            return False
    return True


def find_subsets(seq):
    l = []
    for m in range(len(seq) + 1):
        l += set(combinations(seq, m))
    return l

def sorted_digits(n):
    return "".join(sorted(str(n)))    


def solve():
    result = 0 #@UnusedVariable
    primes = [ p for p in gen_sieve_eratosthenes(10000)]
    primes_4digit = filter(lambda p: len(str(p)) == 4, primes)
   
    # prepare a map of permuted primes
    permuted_primes = {}
    for p in primes_4digit:
        try:
            permuted_primes[sorted_digits(p)] += [p]
        except KeyError, e:
            permuted_primes[sorted_digits(p)] = [p]
    
    # for all lists of permuted primes, check if any subset
    # has the arithmetic property above
    result_candidates = []
    for primes in permuted_primes.values():
        for subset in find_subsets(primes):
            if has_arithmetic_property(subset):
                result_candidates.append("".join(str(p) for p in subset))
    
    result = max(result_candidates) #@UnusedVariable
    print("The concatenated 12-digit number is %(result)s" % vars())

if __name__ == "__main__":
    solve()
