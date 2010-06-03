'''
Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
'''
from sieve import factorize_with_eratosthenes, gen_sieve_eratosthenes
from projecteuler import boolean_product_of

def has_k_primes(n, k, primes):
    l = len(set(factorize_with_eratosthenes(n, primes)))
    return l == k

def solve(N, primes):
    n = 2
    previous_factors_have_k_primes = [False] * N

    LIMIT = primes[-1]**2
    for n in range(2, LIMIT):
        r = has_k_primes(n, N, primes)
        previous_factors_have_k_primes = previous_factors_have_k_primes[1:] + [r]
        if boolean_product_of(previous_factors_have_k_primes):
            return [n+i for i in range(-N+1, 1)]

if __name__ == "__main__":
    consecutive_numbers = solve(4, [p for p in gen_sieve_eratosthenes(1000)])
    print(consecutive_numbers)
    result = consecutive_numbers[0]
    print("Find the first four consecutive integers to have four distinct primes factors. The first of these numbers is %(result)d" % vars())
