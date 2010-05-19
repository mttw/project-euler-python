'''
Find the sum of all the primes below two million.
'''
from sieve import gen_sieve_eratosthenes
from projecteuler import sum_of

def primes_below(ceiling):
    primes = [p for p in gen_sieve_eratosthenes(ceiling)]
    if(primes[-1] > ceiling): 
        return primes[0:-1]
    else:
        return primes

def solve(ceiling):
    return sum_of(primes_below(ceiling))
    
def main():    
    ceiling = 2000000
    result = solve(ceiling)
    print("The sum of all the primes below %(ceiling)d" 
          + " is %(result)d" % vars())



if __name__ == "__main__":
    main()
