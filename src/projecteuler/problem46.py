'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2*1^(2)
15 = 7 + 2*2^(2)
21 = 3 + 2*3^(2)
25 = 7 + 2*3^(2)
27 = 19 + 2*2^(2)
33 = 31 + 2*1^(2)

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

'''
from sieve import gen_sieve_eratosthenes, is_prime

def is_odd(n):
    return n%2 == 1

def calc_goldbach_numbers_dict(N, primes):
    goldbach_numbers = {}
    for p in primes:
        for n in range(1,N):
            gn = p + 2*(n**2)
            goldbach_numbers[gn] = True
    return goldbach_numbers

def solve(N, primes):
    goldbach_nums = calc_goldbach_numbers_dict(N, primes)
    print('Prepared Goldbach numbers')
    L = min(N, primes[-1])
    for i in range(9, L, 2):
        if not i in goldbach_nums and not i in primes: 
            return i
                    

if __name__ == "__main__":
    primes = [p for p in gen_sieve_eratosthenes(10**4)]
    print('Prepared primes')
    result = solve(10**4, primes)
    
    print("The smallest odd composite that cannot be written as the sum of a prime and twice a square is %(result)d" % vars())
