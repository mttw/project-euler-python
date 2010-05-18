import math
from number import lsqrt

def factorize_with_eratosthenes(number):
    primes_in_number = []
    for prime in gen_sieve_eratosthenes(lsqrt(number)):
        while number % prime == 0:
            primes_in_number.append(prime)
            number = number / prime
    if len(primes_in_number) == 0 or number > primes_in_number[-1]:
        primes_in_number.append(number)
    return primes_in_number

def gen_sieve_eratosthenes(ceiling=None):
    if ceiling is not None:
        if ceiling % 2 == 0:
            ceiling -= 1
        highest_prime = math.ceil(math.sqrt(ceiling))
    last_val = 1
    found_primes = []
    yield 2
    while ceiling is None or ceiling > last_val:
        current_val = None
        while current_val is None:
            current_val = last_val = last_val + 2
            for prime, square in found_primes:
                if current_val < square: 
                    break
                if current_val % prime == 0:
                    current_val = None
                    break
        yield current_val
        if ceiling is None or highest_prime > last_val:
            found_primes.append((current_val, current_val ** 2))

