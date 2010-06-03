'''
Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
from sieve import sieve_eratosthenes, gen_sieve_eratosthenes
from itertools import takewhile
import time

def solve(N):
    result = 0 #@UnusedVariable
    primes = sieve_eratosthenes(N)
    print('Number of primes: ' + str(len(primes)))
    
    start = time.clock()
    max_consecutive_primes = [2]
    len_max_consecutive_primes = len(max_consecutive_primes)

    # special treatment for prime sequences starting with 2
    s = 0
    for i in range(0, len(primes)):
        s += primes[i]
        if s in primes:
            max_consecutive_primes = primes[:i+1]
            len_max_consecutive_primes = len(max_consecutive_primes)            
        if s > N: 
            break
    print(len_max_consecutive_primes, sum(max_consecutive_primes), max_consecutive_primes)
    
    # all following sequence lengths must be odd
    if len_max_consecutive_primes % 2 == 0:
        len_max_consecutive_primes += 1

    for i in range(1, len(primes)):
        cons_primes = primes[i:i + len_max_consecutive_primes + 2] 
        cons_sum = sum(cons_primes)

        for j in range(i+ len_max_consecutive_primes + 2, len(primes)-1, 2):
            cons_primes += primes[j:j+2]
            cons_sum += primes[j] + primes[j+1]

            if cons_sum > N:
                break
            if cons_sum in primes:
                max_consecutive_primes = [p for p in cons_primes]
                print(len_max_consecutive_primes, sum(max_consecutive_primes), max_consecutive_primes)
        if i % 5000 == 0:
            print(i, time.clock() - start)
        
    result = sum(max_consecutive_primes)
    print(time.clock() - start)
        
    
    print("The highest prime sum of the most consecutive primes below %(N)d is %(result)d" % vars())




if __name__ == "__main__":
    #solve1(10**4)
    solve(10**6)
