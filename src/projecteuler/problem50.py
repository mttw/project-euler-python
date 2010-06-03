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
    len_max_consecutive_primes += 1
    for i in range(1, len(primes)):
        cons_primes = primes[i:i + len_max_consecutive_primes + 2] 
        len_cons_primes = len(cons_primes)
        cons_sum = sum(cons_primes)
#        print('***', i, i+ len_max_consecutive_primes)
#        print('***', primes[i+ len_max_consecutive_primes], cons_primes)

        for j in range(i+ len_max_consecutive_primes + 2, len(primes)-1, 2):
            cons_primes.append(primes[j])
            cons_primes.append(primes[j+1])
            cons_sum += primes[j]
            cons_sum += primes[j+1]
#            print('###', primes[j], primes[j+1])
            len_cons_primes += 2

            if cons_sum > N:
                break
            if cons_sum in primes and len_cons_primes > len_max_consecutive_primes:
                max_consecutive_primes = cons_primes
                len_max_consecutive_primes = len_cons_primes 
                print(len_max_consecutive_primes, sum(max_consecutive_primes), max_consecutive_primes)
        if i % 1000 == 0:
            print(i, primes[i], time.clock() - start)
            start = time.clock()
        
    result = len_max_consecutive_primes 
    print(time.clock() - start)
        
    
    print("The longest sequence of consecutive primes below %(N)d is %(result)d" % vars())


def solve1(N):
    result = 0 #@UnusedVariable
    primes = sieve_eratosthenes(N)
    print('Number of primes: ' + str(len(primes)))
    
    start = time.clock()
    max_consecutive_primes = [2]
    len_max_consecutive_primes = len(max_consecutive_primes)

    s = 0
    for i in range(0, len(primes)):
        s += primes[i]
        if s in primes:
            max_consecutive_primes = primes[:i+1]
            len_max_consecutive_primes = len(max_consecutive_primes)            
        if s > N: 
            break
    print(len_max_consecutive_primes, sum(max_consecutive_primes), max_consecutive_primes)
    for i in range(1, len(primes)):
        cons_primes = [primes[i]] 
        len_cons_primes = 1
        cons_sum = sum(cons_primes)

        for j in range(i+1, len(primes)-1, 2):
            cons_primes.append(primes[j])
            cons_primes.append(primes[j+1])
            cons_sum += primes[j]
            cons_sum += primes[j+1]
            len_cons_primes += 2

            if cons_sum > N:
                break
            if cons_sum in primes and len_cons_primes > len_max_consecutive_primes:
                max_consecutive_primes = cons_primes
                len_max_consecutive_primes = len(cons_primes) 
                print(len_max_consecutive_primes, sum(max_consecutive_primes), max_consecutive_primes)
        if i % 1000 == 0:
            print(i, primes[i], time.clock() - start)
            start = time.clock()
        
    result = len_max_consecutive_primes 
    print(time.clock() - start)
        
    
    print("The longest sequence of consecutive primes below %(N)d is %(result)d" % vars())

#
#def solve2(N):
#    result = 0 #@UnusedVariable
#    primes = list(gen_sieve_eratosthenes(N))
#    print('Number of primes: ' + str(len(primes)))
#    
#    start = time.clock()
#    max_consecutive_primes = [2]
#    s = 0
#    for i in range(0, len(primes)):
#        s += primes[i]
#        print(primes[:i+1])
#        if s > N: 
#            break
#        if s in primes:
#            max_consecutive_primes = primes[:i+1]
#    print(max_consecutive_primes)
#    print(sum(max_consecutive_primes)) 
#    
#    for i in range(1, len(primes)):
#        l = i+len(max_consecutive_primes)
#        cons_primes = primes[i:l+1] 
#        cons_sum = sum(cons_primes)
#        for j in range(i+l, len(primes), 2):
#            cons_primes.append(primes[j])
#            cons_primes.append(primes[j+1])
#            cons_sum += primes[j] + primes[j+1]
#            
#            if cons_sum in primes:
#                # cons_primes is always larger than previous ones
#                print(cons_primes)
#                print(sum(cons_primes), cons_sum)
#                max_consecutive_primes = cons_primes 
#            if cons_sum > N:
#                break
#        if i % 1000 == 0:
#            print(i, primes[i], time.clock() - start)
#            start = time.clock()
#        
#    result = sum(max_consecutive_primes) 
#    print(max_consecutive_primes)
#    print(result)
#    print(time.clock() - start)
#        
#    
#    print("The longest sequence of consecutive primes below %(N)d is %(result)d" % vars())

if __name__ == "__main__":
    #solve1(10**4)
    solve(10**6)
